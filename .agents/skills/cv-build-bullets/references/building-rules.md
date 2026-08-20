# Content-first CV bullet rules

## Evidence and integrity

- Use only facts supported by pasted or current bullet wording, facts explicitly supplied by the user, or context sources the user explicitly authorised the skill to read.
- Treat optional context as corroboration or additional evidence, not as a mandatory input.
- Never invent or strengthen metrics, scale, ownership, technologies, outcomes, or business impact.
- Omit unsupported metrics; never insert placeholders such as `[X%]`.
- Resolve material conflicts before editing.
- Exclude credentials, personal information, internal identifiers, and confidential implementation details unsuitable for a public CV.

## Strong technical content

- Start with an accurate action verb and use concise British English.
- Apply the XYZ principle naturally: communicate the achievement, its measured result when supported, and the technical mechanism.
- Lead with the most differentiating result or engineering contribution rather than a duty.
- Name technologies when they explain how the result was achieved, not as a detached keyword list.
- Preserve useful detail about architecture, algorithms, data, scale, reliability, performance, security, testing, automation, or ownership.
- Give every bullet a distinct purpose and avoid repeated opening verbs, claims, metrics, and tool lists.
- Prefer clear technical language to grandiose or unusual verbs. Avoid first-person pronouns, vague praise, filler, keyword stuffing, and unverifiable adjectives such as “top 5%”.
- Metrics may quantify performance, scale, reliability, coverage, latency, cost, adoption, delivery, or accuracy. A bullet remains valid without a metric when its technical contribution is strong and evidence-backed.

## Content-first length

- Do not apply a default character ceiling or force a bullet into one line.
- Retain the strongest supported causal chain even when it requires two or three rendered lines.
- Remove genuine repetition and filler, but do not discard important mechanism merely to imitate a short final-layout bullet.
- Use `$cv-fit-bullets` in a separate request when the user wants one-line bullets, a specific line count, or a one-page CV.

## LaTeX

- In CV edit mode, change only the inner content of each existing `\resumeItem{...}` slot and preserve every wrapper and surrounding byte.
- In prompt-only mode, preserve any pasted `\resumeItem{...}` wrappers and modify only their inner text.
- Escape literal `%`, `&`, `_`, `#`, and `$` characters.
- Keep each replacement as one logical bullet and preserve the existing bullet count and order.

## Guidance basis

- Google recommends showing an accomplishment, a measurement when available, and how it was achieved.
- MIT career guidance recommends strong action verbs, relevant tasks, outcomes, metrics, and one-to-two-line final resume bullets. This skill deliberately handles the richer content-first draft before final fitting.
