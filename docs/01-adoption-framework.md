# Adoption Framework

A 90-day phased rollout for a small license pool (25–150 seats) run by one person.

## Phase 0 — Before you assign a single license (2 weeks)

The failure mode here is assigning licenses to whoever asked loudest. Do this instead:

1. **Baseline survey.** Ask people what eats their week. Use `templates/surveys/readiness-survey.md`. You are collecting two things: candidate use cases, and named volunteers.
2. **Pick the pilot cohort on task fit, not seniority.** The best early adopters are people who write, summarize, or reconcile documents daily. Heavy-meeting roles are good too. People who live in a single line-of-business application all day are the worst first cohort — Copilot has nothing to grab onto.
3. **Set the denominator and write it down.** See `02-metrics-and-reporting.md`. Do this before anyone can move the goalposts.
4. **Get the governance answers in writing** before the first question comes from the floor: what data can go in, what the retention story is, whether prompts are logged. `06-governance.md`.
5. **Capture "before" metrics for 3–5 use cases.** This is the single most-skipped step and the one that makes or breaks your ROI case six months later. Five minutes of stopwatch data now is worth a hundred slides later.

## Phase 1 — Land it (weeks 1–4)

| Week | Action |
|---|---|
| 1 | Launch announcement (`templates/comms/launch-announcement.md`). One 30-minute live session per department, not one giant all-hands. |
| 2 | Training Phase 1 delivered (see `04-training-program.md`). First weekly adoption report published even though the numbers look bad. |
| 3 | Identify champions from usage data + session participation. First champion spotlight published. |
| 4 | First license reallocation conversation. Publish the prompt gallery. |

The point of week 2's ugly report is credibility. If your first report is the one where the numbers are good, nobody believes any of them.

## Phase 2 — Make it stick (weeks 5–8)

- **2-Week Challenge** (`templates/comms/challenge-kickoff.md`). Low stakes, department-vs-department, tiny prizes. This reliably converts the passive middle.
- **Department-specific prompt sessions.** Generic training gets you to "I tried it." Department prompts get you to "I use it."
- **Office hours instead of training.** By week 5, people have specific problems. Standing 30-minute drop-in beats another curriculum.
- **Start the dormant-license conversation.** Two weeks of zero activity → a friendly check-in, not a reclaim threat. Reclaim at week 4 of zero activity.

## Phase 3 — Institutionalize (weeks 9–12)

- Publish a 90-day impact report with the ROI model and your before/after data.
- Convert your best 3 workflows from "prompt someone types" into something automated — an agent, a flow, a template. Prompts that get used 20 times a week should not be retyped.
- Hand each department one named owner for their prompt gallery section.
- Set the recurring cadence: weekly report, monthly spotlight, quarterly impact review.

## What actually predicts adoption

Ranked by observed impact, strongest first:

1. A specific, named task the person does weekly
2. Peer proof from someone in the same role
3. Ease of first success (the first attempt must work)
4. Manager visibly using it
5. Training content quality

Note that training quality is last. Most adoption programs invert this list.
