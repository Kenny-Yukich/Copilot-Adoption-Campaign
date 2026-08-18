#!/usr/bin/env python3
"""
adoption_report.py — turn a Copilot usage CSV export into a weekly adoption report.

Standard library only. No pip install, no request to IT.

The point of this script is not sophistication, it's determinism: the same input
produces the same numbers every week, so a change in the report means a change in
behavior rather than a change in how you did the arithmetic.

Usage:
    python3 adoption_report.py <usage.csv> [--config config.json] [--out out/] [--week 21]

Outputs:
    out/adoption-report-week<N>.md   Report, ready to paste or convert
    out/dormant-week<N>.csv          Follow-up list of zero-activity licenses
"""

import argparse
import csv
import json
import os
import statistics
import sys
from collections import defaultdict
from datetime import date

DEFAULT_CONFIG = {
    "user_column": "UserPrincipalName",
    "department_column": "Department",
    # Columns holding per-app action counts. Any column ending in the suffix below
    # is treated as an app activity column, so you don't have to list them all.
    "activity_column_suffix": "CopilotActions",
    "activity_columns": [],
    # Users excluded from the denominator. Use roles/accounts, not people you
    # dislike. Program owner belongs here — your own usage inflates the number.
    "exclude_users": [],
    # Override the denominator if licenses are assigned but absent from the export.
    "denominator_override": None,
    "target_active_rate": 90.0,
    "data_source": "<name your source>",
    "window": "rolling 28-day",
    "dormant_followup_threshold": 0,
}


def load_config(path):
    cfg = dict(DEFAULT_CONFIG)
    if path and os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            cfg.update(json.load(f))
    return cfg


def detect_activity_columns(fieldnames, cfg):
    if cfg["activity_columns"]:
        missing = [c for c in cfg["activity_columns"] if c not in fieldnames]
        if missing:
            sys.exit(f"ERROR: configured activity columns not in CSV: {missing}")
        return cfg["activity_columns"]
    suffix = cfg["activity_column_suffix"]
    cols = [c for c in fieldnames if c.strip().endswith(suffix)]
    if not cols:
        sys.exit(
            f"ERROR: no columns ending in '{suffix}'. Set 'activity_columns' "
            f"explicitly in your config. Columns found: {fieldnames}"
        )
    return cols


def to_int(value):
    try:
        return int(float(str(value).strip() or 0))
    except ValueError:
        return 0


def app_name(column, suffix):
    name = column.strip()
    if name.endswith(suffix):
        name = name[: -len(suffix)]
    return name or column


def analyze(rows, activity_cols, cfg):
    excluded = {u.strip().lower() for u in cfg["exclude_users"]}
    users, skipped = [], 0

    for row in rows:
        upn = (row.get(cfg["user_column"]) or "").strip()
        if not upn:
            continue
        if upn.lower() in excluded:
            skipped += 1
            continue
        per_app = {c: to_int(row.get(c)) for c in activity_cols}
        total = sum(per_app.values())
        users.append(
            {
                "upn": upn,
                "dept": (row.get(cfg["department_column"]) or "Unassigned").strip(),
                "per_app": per_app,
                "total": total,
                "apps_used": sum(1 for v in per_app.values() if v > 0),
                "active": total > 0,
            }
        )

    denominator = cfg["denominator_override"] or len(users)
    active = [u for u in users if u["active"]]
    dormant = [u for u in users if not u["active"]]

    by_dept = defaultdict(lambda: {"total": 0, "active": 0, "actions": 0})
    for u in users:
        d = by_dept[u["dept"]]
        d["total"] += 1
        d["active"] += 1 if u["active"] else 0
        d["actions"] += u["total"]

    app_totals = {
        app_name(c, cfg["activity_column_suffix"]): sum(u["per_app"][c] for u in users)
        for c in activity_cols
    }
    app_users = {
        app_name(c, cfg["activity_column_suffix"]): sum(
            1 for u in users if u["per_app"][c] > 0
        )
        for c in activity_cols
    }

    return {
        "counted": len(users),
        "skipped": skipped,
        "denominator": denominator,
        "active_users": len(active),
        "active_rate": (len(active) / denominator * 100) if denominator else 0.0,
        "dormant": sorted(dormant, key=lambda u: (u["dept"], u["upn"])),
        "median_actions": statistics.median([u["total"] for u in active]) if active else 0,
        "median_apps": statistics.median([u["apps_used"] for u in active]) if active else 0,
        "total_actions": sum(u["total"] for u in users),
        "by_dept": dict(by_dept),
        "app_totals": app_totals,
        "app_users": app_users,
        "top_users": sorted(active, key=lambda u: -u["total"])[:5],
    }


def render(stats, cfg, week):
    tgt = cfg["target_active_rate"]
    gap = stats["active_rate"] - tgt
    L = []
    a = L.append

    a(f"# Weekly Copilot Adoption Report — Week {week}, {date.today().year}")
    a("")
    a(
        f"**Data source:** {cfg['data_source']} · **Window:** {cfg['window']} · "
        f"**Generated:** {date.today().isoformat()}"
    )
    a(
        f"**Denominator:** {stats['counted'] + stats['skipped']} rows in export, "
        f"{stats['skipped']} excluded → **{stats['denominator']} counted**"
    )
    a("")
    a("## 1. The number")
    a("")
    a("| Metric | This week | Target |")
    a("|---|---|---|")
    a(f"| Active rate | **{stats['active_rate']:.1f}%** | {tgt:.0f}% |")
    a(f"| Active users | {stats['active_users']} of {stats['denominator']} | — |")
    a(f"| Median actions per active user | {stats['median_actions']:.0f} | — |")
    a(f"| Median apps used per active user | {stats['median_apps']:.0f} | — |")
    a(f"| Dormant licenses | {len(stats['dormant'])} | 0 |")
    a(f"| Total actions in window | {stats['total_actions']:,} | — |")
    a("")
    status = "at or above target" if gap >= 0 else f"{abs(gap):.1f} points below target"
    a(
        f"**One-line read:** {stats['active_users']} of {stats['denominator']} licensed "
        f"users were active in the {cfg['window']} window ({stats['active_rate']:.1f}%), "
        f"{status}; {len(stats['dormant'])} licenses show zero activity."
    )
    a("")
    a("## 2. By department")
    a("")
    a("| Department | Licensed | Active | Rate | Actions |")
    a("|---|---|---|---|---|")
    for dept, d in sorted(
        stats["by_dept"].items(),
        key=lambda kv: -(kv[1]["active"] / kv[1]["total"] if kv[1]["total"] else 0),
    ):
        rate = (d["active"] / d["total"] * 100) if d["total"] else 0
        a(f"| {dept} | {d['total']} | {d['active']} | {rate:.0f}% | {d['actions']:,} |")
    a("")
    a("## 3. By application")
    a("")
    a("| App | Users | Actions |")
    a("|---|---|---|")
    for app, total in sorted(stats["app_totals"].items(), key=lambda kv: -kv[1]):
        a(f"| {app} | {stats['app_users'][app]} | {total:,} |")
    a("")
    a("Low-usage apps are a training gap, not a product problem. Breadth is the")
    a("metric that predicts retention — single-app users churn back to old habits.")
    a("")
    a("## 4. Dormant licenses")
    a("")
    if stats["dormant"]:
        a(f"{len(stats['dormant'])} licenses with zero activity this window:")
        a("")
        a("| Department | User |")
        a("|---|---|")
        for u in stats["dormant"]:
            a(f"| {u['dept']} | {u['upn']} |")
        a("")
        a("Full list also written to the dormant CSV for follow-up tracking.")
        a("")
        a("Suggested handling: friendly check-in at 2 consecutive dormant weeks,")
        a("reallocation conversation at 4. Frame it as service, not enforcement.")
    else:
        a("None. Every assigned license shows activity this window.")
    a("")
    a("## 5. Actions this week")
    a("")
    a("| Action | Who | By when |")
    a("|---|---|---|")
    a("|  |  |  |")
    a("")
    a("---")
    a("")
    a(
        "*Generated by adoption_report.py. Hours-returned and ROI estimates are "
        "published quarterly, not weekly — weekly ROI estimates are noise.*"
    )
    return "\n".join(L) + "\n"


def main():
    p = argparse.ArgumentParser(description="Generate a weekly Copilot adoption report.")
    p.add_argument("csv_path", help="Usage export CSV")
    p.add_argument("--config", default="config.json")
    p.add_argument("--out", default="out")
    p.add_argument("--week", default=None, help="Week number for the report title")
    args = p.parse_args()

    cfg = load_config(args.config)

    with open(args.csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            sys.exit("ERROR: CSV appears to be empty.")
        if cfg["user_column"] not in reader.fieldnames:
            sys.exit(
                f"ERROR: user column '{cfg['user_column']}' not found. "
                f"Columns: {reader.fieldnames}"
            )
        activity_cols = detect_activity_columns(reader.fieldnames, cfg)
        rows = list(reader)

    stats = analyze(rows, activity_cols, cfg)
    week = args.week or date.today().isocalendar()[1]

    os.makedirs(args.out, exist_ok=True)
    report_path = os.path.join(args.out, f"adoption-report-week{week}.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(render(stats, cfg, week))

    dormant_path = os.path.join(args.out, f"dormant-week{week}.csv")
    with open(dormant_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Department", "User", "WeeksDormant", "ActionTaken", "FollowUpDate"])
        for u in stats["dormant"]:
            w.writerow([u["dept"], u["upn"], "", "", ""])

    print(f"Active rate: {stats['active_rate']:.1f}% "
          f"({stats['active_users']}/{stats['denominator']})")
    print(f"Dormant: {len(stats['dormant'])}  |  Excluded: {stats['skipped']}")
    print(f"Apps detected: {', '.join(stats['app_totals'])}")
    print(f"\nWrote {report_path}\nWrote {dormant_path}")


if __name__ == "__main__":
    main()
