# Job-description tailoring rules

## Truth before keyword coverage

- Never add a technology, method, responsibility, level of ownership, metric, or domain claim merely because it appears in the job description.
- Insert a keyword only when the relevant experience evidence supports the same substantive meaning.
- Equivalent terminology may be substituted when accurate, such as expanding an evidenced abbreviation to the job description's full phrase.
- Treat unsupported requirements as gaps to report, not prose to manufacture.

## Natural relevance

- Prioritise must-have requirements and core responsibilities over incidental repeated words.
- Use a job-description phrase only when it makes the bullet more precise or recognisable.
- Preserve the achievement and technical causal chain; do not turn bullets into keyword lists.
- Prefer concrete nouns and industry-standard terms to vague synonyms.
- Retain strong evidence even when it is not repeated in the vacancy if it differentiates the candidate.
- Avoid copying long phrases or company marketing language verbatim.

## Bullet quality

- Start with an accurate action verb.
- State the result or contribution, supported measurement when available, and technical mechanism in a natural order.
- Preserve British English and concise sentence fragments.
- Remove vague duties, repetition, filler, and unsupported adjectives.
- Keep distinct bullets focused on distinct achievements.

## Footprint

- Preserve the rendered line count of every edited bullet.
- Aim for no more than a three-visible-character difference from the corresponding source bullet until actual PDF rendering is available.
- Character equality is not proof of layout equality: bold text, punctuation, and wide glyphs affect proportional-font width.
- When the footprint and a keyword insertion conflict, preserve truth and layout; report the omitted keyword.

## Scope and LaTeX

- Draft against only the private `applications/<slug>/main.tex` copy and never mutate its bullets before approval.
- Preserve active bullet count and ordering in `proposed_bullets`.
- Escape literal LaTeX-sensitive characters.
- Do not add bold formatting as part of tailoring; use `$cv-bold-highlights` separately.
