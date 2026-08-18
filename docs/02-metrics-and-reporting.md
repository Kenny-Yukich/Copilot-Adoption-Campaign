# Metrics and Reporting

## Rule 1: Never conflate two data sources with different windows

This is the mistake that will cost you the most credibility, and it is very easy to make.

Copilot usage data is available from multiple surfaces, and **they use different time windows and different definitions of "active."** A rolling 28-day window and a fixed 7-day export will disagree, and the disagreement is not an error — it is the definition.

Consequences to internalize:

- Pick **one** source of truth per report and label it in the report header, including the window.
- Never mix a number from one surface with a number from another in the same chart.
- When leadership asks "why did adoption drop," check whether the window shifted before you check whether behavior changed.
- Field names and availability in these reports change between product releases. Re-verify before you build automation on a specific column.

## Rule 2: Write the denominator down and get it agreed

"92% adoption" means nothing until you define the population. Decide and document:

| Decision | Typical answer |
|---|---|
| Who is in the denominator? | All assigned licenses as of the report date |
| Do you exclude admin/test/service accounts? | Yes — list them explicitly by role, not name |
| Do you exclude the program owner? | Yes. Your own usage inflates the number and everyone knows it |
| What counts as "active"? | At least one Copilot action in any app during the window |
| What about mid-window license assignment? | Excluded until they've held the license the full window |

Put this in a `standing-context` file next to your reporting script so the rules survive you having a bad week.

## Rule 3: Report a small number of stable metrics

**Core four, every week:**

1. **Active rate** — active users ÷ denominator, with the window named
2. **Depth** — median actions per active user (catches the "logged in once" illusion)
3. **Breadth** — number of distinct apps used per active user
4. **Dormant count** — assigned licenses with zero activity, and how many weeks running

**Quarterly only:**

- Department penetration
- Use-case inventory (how many documented workflows exist)
- Reclaimed/reallocated licenses
- Estimated hours returned (ROI model — always labeled as an estimate)

## Anti-metrics

Metrics that look good and teach you nothing:

- Total prompts submitted (gameable, and it rewards inefficiency)
- Training attendance (attendance is not adoption)
- Survey satisfaction with no behavioral pairing
- Any percentage without a denominator in the same sentence

## Reporting cadence and format

Same layout every week, one page, three sections: **number, movement, action.** Executives read the first section, managers read the second, you act on the third.

Use `templates/reports/weekly-adoption-report-template.md`, and generate the numbers with `scripts/adoption_report.py` so the calculation is identical week over week. Manual calculation drifts, and drift is indistinguishable from lying.
