# CV bullet building rules

## Evidence and integrity

- Use only facts supported by readable files in the target employer folder or supplied directly by the user.
- Never invent or strengthen metrics, scale, ownership, technologies, outcomes, or business impact.
- Omit a metric when none is supported. Do not insert placeholders such as `[X%]`.
- Resolve ambiguous or contradictory evidence with the user before editing.
- Exclude confidential implementation details, personal data, credentials, and internal identifiers that are unsuitable for a public CV.

## Content

- Write for competitive software-engineering roles with concrete technical specificity.
- Apply Google's XYZ principle naturally: communicate what was achieved, how it was measured when evidence exists, and how it was done.
- Do not force one fixed sentence order. Prefer natural forms such as “Reduced X by Y by implementing Z” or “Built Z to achieve X”.
- Start with a strong, accurate action verb and use concise British English.
- Emphasize engineering decisions, systems, technologies, scale, reliability, performance, automation, security, or user impact when supported.
- Give each bullet a distinct purpose. Avoid repeating the same achievement, metric, technology list, or opening verb.
- Avoid first-person pronouns, vague praise, keyword stuffing, filler, and unverifiable adjectives.
- Match the concise, metric-consistent quality demonstrated by the Sign Language Fingerspelling Recognition System bullets in `cv_main.tex` without copying their wording.

## Length

- Limit each bullet to 113 rendered characters, including spaces and punctuation.
- Ignore non-rendered LaTeX syntax when counting. Count escaped characters by their displayed form; for example, count `\%` as `%` and `\&` as `&`.
- Aim as close to 113 characters as useful evidence permits, preferably 105–113 characters.
- Never add filler, duplicate facts, or weaken clarity merely to approach the limit.

## LaTeX

- Preserve the existing `\resumeItem{...}` wrapper and all surrounding LaTeX structure.
- Escape LaTeX-sensitive characters in generated prose, including `%`, `&`, `_`, `#`, and `$` when they are intended literally.
- Keep each bullet as one logical `\resumeItem` entry.
