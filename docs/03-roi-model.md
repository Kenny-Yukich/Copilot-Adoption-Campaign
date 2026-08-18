# ROI Model

## What this is and isn't

This is a **defensible estimation framework**. It is not measurement. Label it that way in every deliverable — the moment a CFO catches you presenting an estimate as a measurement, every number you produce afterward is discounted.

The goal is not to prove a number. The goal is to survive scrutiny of your assumptions.

## The model

```
Annual hours returned = Active users
                      × Workflows per user
                      × Uses per workflow per week
                      × Minutes saved per use
                      × 46 working weeks
                      ÷ 60
```

```
Gross annual value  = Annual hours returned × Fully burdened hourly rate
Annual cost         = Licensed seats × Annual license cost + Program overhead
Net value           = Gross annual value − Annual cost
ROI %               = Net value ÷ Annual cost × 100
```

## The assumptions that get challenged, and how to survive them

| Assumption | The challenge you'll get | How to defend it |
|---|---|---|
| Minutes saved per use | "You made that up" | Stopwatch 5 real before/after pairs. Five real data points beats any benchmark |
| Uses per week | "That's optimistic" | Take it from usage data, not from a survey |
| 46 working weeks | — | Rarely challenged. 52 minus PTO/holidays |
| Fully burdened rate | "Use base salary" | Use whatever your finance team uses for internal project costing. Ask them, then cite them |
| Realization rate | "Saved time isn't recovered value" | **This is the real challenge.** Answer it head-on, below |

## The realization-rate problem

Saved minutes are not automatically money. If someone saves 20 minutes and spends it on a longer coffee break, you produced nothing measurable.

Handle it by applying an explicit realization haircut — 50% is a conservative, hard-to-argue-with default — and by classifying value into three tiers:

1. **Hard capacity** (highest credibility): work that used to require overtime, contractors, or a backfill and now doesn't. Rare, but this is the tier that funds programs.
2. **Redirected capacity** (medium): time measurably moved to a named higher-value activity. Requires the person to tell you where it went.
3. **Quality/latency improvement** (real but soft): faster response times, fewer errors, better-documented decisions. Report as narrative, not dollars.

Report all three. Lead with tier 1 if you have any. Never sum them into a single number without showing the split.

## Presenting it

- Show a **range**, not a point estimate. Conservative / expected / optimistic, with the assumption that changes between them called out.
- Include a **break-even line**: "this pays for itself at X minutes saved per user per week." That single sentence is often more persuasive than the whole model, because it converts an abstract argument into an intuition check.
- Include the **cost of dormant licenses** as a negative line item. It shows you're managing the spend, not just advocating for it.
- Benchmark against a published third-party study if you cite one — and cite it properly with the date, because these figures age.

## Worked example (usage data only)

| Input | Value |
|---|---|
| Active users | 60 |
| Workflows per user | 2 |
| Uses per workflow per week | 3 |
| Minutes saved per use | 12 |
| Realization rate | 50% |
| Working weeks | 46 |

Hours returned: 60 × 2 × 3 × 12 × 46 ÷ 60 = 3,312 → × 50% = **1,656 hours**
Break-even: roughly **4 minutes saved per active user per week.**

To finish the financial analysis, obtain your organization's approved fully burdened
rate, annual license cost, and program overhead from Finance, then apply the formulas
above. Keep those internal figures out of public copies of this kit.

The break-even line is the one to put on the slide.
