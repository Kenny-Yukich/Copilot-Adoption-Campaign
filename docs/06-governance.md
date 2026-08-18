# Governance and Guardrails

Answer these before your first training session, in writing, in language a non-technical employee can read. If you can't answer one, say so plainly and say who's working on it.

## Questions you will be asked in the first week

1. **Can it see my files?** — It can surface content the user already has permission to access. It does not grant new access. Say this precisely, because a vague answer here reads as a dodge.
2. **Are my prompts being read?** — Explain what is logged, who can access it, and under what circumstances. Get the real answer from your tenant admin rather than guessing.
3. **Does anything leave the tenant?** — Know your actual configuration and licensing terms. Don't paraphrase marketing copy.
4. **Is this going to eliminate my job?** — Answer directly. A hedge here does more damage than any technical limitation.
5. **What happens if it's wrong?** — Establish the verification expectation explicitly: the person who sends the output owns the output.

## Pre-rollout technical prerequisites

The uncomfortable truth: **Copilot exposes your permissions hygiene.** Oversharing that existed invisibly for years becomes discoverable the moment search gets good.

- Audit broad-permission sites and libraries before rollout, not after
- Review "anyone with the link" sharing
- Check for sensitive content sitting in locations with loose permissions (HR, finance, legal, IP)
- Confirm retention and eDiscovery coverage for AI interactions with whoever owns compliance
- Verify sensitivity labeling behavior if you use it

Budget real time for this. It is the most common cause of a rollout getting paused mid-flight.

## Acceptable-use guidance for end users

Keep it to one page. Suggested content:

**Do:** use it on work you can verify; use it for drafts, summaries, and reformatting; cite it when it materially shaped a deliverable that goes to a customer.

**Don't:** paste in data you wouldn't email internally; rely on it for calculations without checking; use it for decisions requiring professional judgment or credentialing; treat output as reviewed just because it reads well.

**Always:** verify names, numbers, dates, quotes, and anything a customer will act on.

## For the AI program owner

- Keep a decision log. Six months in you will not remember why you excluded a group from the denominator, and someone will ask.
- Escalate anything touching regulated data, IP, or customer contracts to whoever owns that risk. Don't absorb it because absorbing it is faster.
- Get explicit clearance before publishing anything externally that was built on work time. Ownership of work product is rarely ambiguous, and "it's generic now" is not a clearance.
