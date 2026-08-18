# scripts

## adoption_report.py

Turns a usage CSV into a weekly adoption report plus a dormant-license follow-up list. Standard library only.

```bash
cp config.example.json config.json
python3 adoption_report.py sample-data/sample_copilot_usage.csv --config config.json --week 21
```

### Expected CSV shape

One row per licensed user. Required: a user column and a department column. Activity columns are **auto-detected** by suffix — any column ending in `CopilotActions` (configurable) is treated as a per-app action count, so you don't have to update the config when the export adds an app.

```
UserPrincipalName,Department,TeamsCopilotActions,OutlookCopilotActions,WordCopilotActions,...
```

If your export uses different names, either rename the headers or set `activity_columns` explicitly.

### Config

| Key | Purpose |
|---|---|
| `exclude_users` | Removed from the denominator. Put your own account here — your usage inflates the number and everyone knows it |
| `denominator_override` | Use when licenses are assigned but missing from the export |
| `target_active_rate` | Drives the target column and the one-line read |
| `data_source` / `window` | Printed in the report header. **Fill these in.** A report without a stated window invites invalid week-over-week comparisons |

### Notes

- `config.json` and `out/` are gitignored. Real exports contain user identities — never commit them.
- "Active" means at least one action in any app during the window. If you change that definition, change it in `analyze()` and note the change in the report header, because your trend line breaks.
- `--week` sets the report title and output filenames; defaults to the current ISO week.
