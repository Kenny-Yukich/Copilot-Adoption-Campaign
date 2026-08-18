# Contributing

## Ground rules

1. **No employer-identifying content.** No company names, employee names, internal URLs, tenant IDs, license counts, ERP or line-of-business system names, or real usage metrics. If a prompt only makes sense at one company, generalize it or leave it out.
2. **No screenshots of internal tools.** Product UI changes anyway.
3. **Real metrics get replaced with illustrative ones**, clearly labeled.

## Contributing a prompt

Add a row to `templates/prompt-gallery/prompt-gallery.csv`:

- `Department` — use an existing value if one fits
- `Task` — the job to be done, in the user's language ("Turn a supplier email thread into a decision summary")
- `Prompt` — the actual text, with `[BRACKETED]` placeholders for anything user-specific
- `App` — where it runs (Word, Excel, Outlook, Teams, Copilot Chat, PowerPoint)
- `Level` — Starter / Intermediate / Advanced
- `Est. Time Saved` — your honest estimate per use, in minutes

A good prompt names the role, the input, the output format, and the constraint. A bad prompt is a question you could have typed into a search bar.

## Contributing docs or scripts

Open an issue first for anything structural. Scripts stay standard-library-only so they run anywhere without a pip install request going to IT.

## Pre-publish checklist for your own fork

- [ ] `git grep -i` your company name, product names, and colleagues' surnames — expect to find at least one
- [ ] Check CSV/XLSX files, not just markdown
- [ ] Check commit messages and author email
- [ ] Confirm with whoever owns IP at your employer before publishing anything derived from work you did on the clock
