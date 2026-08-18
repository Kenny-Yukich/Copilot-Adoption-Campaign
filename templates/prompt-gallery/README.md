# Prompt Gallery

`prompt-gallery.csv` is a department-organized starter library. It exists because generic training produces "I tried it" and department-specific prompts produce "I use it."

## Columns

| Column | Notes |
|---|---|
| Department | Rename to match your org chart |
| Task | Phrased as the job to be done, in the user's words |
| Prompt | `[BRACKETED]` placeholders are user-supplied |
| App | Where it runs |
| Level | Starter / Intermediate / Advanced |
| Est. Time Saved (min) | Honest per-use estimate. Feeds the ROI model |

## Publishing it

Import the CSV into a SharePoint list, filter by department, and surface each department's view on their own team site. Two things matter more than the platform:

1. **Each department sees only their prompts by default.** A 400-row list nobody filters gets used once.
2. **Each department has a named owner** who can add rows. A gallery only IT can edit is a gallery that goes stale in a month.

Track which prompts actually get used if your platform allows it — usually 5–8 prompts account for most of the value, and knowing which ones tells you what to automate next.

## Writing good prompts

Four parts: **role, input, output format, constraint.**

> Weak: "Summarize this."
>
> Strong: "You are reviewing a supplier quote. Summarize the attached document into a five-bullet decision brief covering price, lead time, payment terms, exclusions, and anything unusual. Flag anything that differs from a standard quote. Do not infer values that aren't stated."

The constraint clause — "do not infer values that aren't stated" — is what separates output you can trust from output you have to re-verify line by line.
