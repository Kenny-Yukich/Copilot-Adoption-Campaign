# M365 Copilot Adoption Kit

A field-tested toolkit for driving Microsoft 365 Copilot adoption in a mid-size organization — built and run by a one-person AI enablement function, not a consulting engagement.

Most Copilot adoption content is either vendor marketing or enterprise change-management theory written for companies with a dedicated CoE. This kit is the opposite: it assumes you are one person with a license pool, a spreadsheet, and a leadership team that wants numbers.

## What's in here

| Folder | What it gives you |
|---|---|
| `docs/` | The framework: phased rollout, metrics definitions, ROI model, training program, community playbook, governance guardrails |
| `templates/prompt-gallery/` | A department-by-department prompt library (11 departments, ready to import into SharePoint or a wiki) |
| `templates/comms/` | Launch announcement, weekly tip email, champion spotlight, 2-week challenge kickoff |
| `templates/reports/` | Weekly adoption report template that survives an executive skim |
| `templates/surveys/` | Pre-rollout readiness survey and post-training pulse |
| `scripts/` | `adoption_report.py` — turns a usage CSV export into a markdown adoption report plus a dormant-user follow-up list |

## Quick start

```bash
git clone https://github.com/Kenny-Yukich/Copilot-Adoption-Campaign.git
cd Copilot-Adoption-Campaign/scripts
cp config.example.json config.json     # set your denominator, exclusions, target
python3 adoption_report.py sample-data/sample_copilot_usage.csv --config config.json
```

No dependencies — standard library only. Output lands in `scripts/out/`.

## The short version of the method

1. **Define the denominator before you report anything.** Adoption percentages are meaningless until you agree on who counts. See `docs/02-metrics-and-reporting.md`.
2. **Train the task, not the tool.** Nobody adopts "Copilot." They adopt "summarize this 40-page spec into a punch list." The prompt gallery exists for this reason.
3. **Report weekly, same format, forever.** Consistency beats sophistication. Leadership learns to read one layout and starts asking better questions.
4. **Find your champions in week 2 and make them visible.** Peer proof outperforms IT proof roughly every time.
5. **Reclaim licenses without drama.** A dormant license is a budget argument against you. Move it to someone on the waitlist.

## Scope and honesty notes

- User and activity numbers in the docs and sample data are **illustrative and synthetic**. Substitute your own.
- Public examples intentionally omit dollar amounts. Add organization-approved financial inputs only in private working copies.
- The ROI model is a defensible estimation framework, not a measurement. It is labeled as such so nobody gets ambushed in a budget meeting.
- Nothing here is Microsoft-official. Product surfaces, admin center reports, and Viva Insights fields change frequently — verify current field names against Microsoft Learn before you build on them.

## License

MIT — see [LICENSE](LICENSE). Use it, fork it, strip the parts that don't fit your org.

## Contributing

Prompt contributions are the most useful thing you can send. See [CONTRIBUTING.md](CONTRIBUTING.md).
