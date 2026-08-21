# CV bullet fitting rules

## Preserve meaning

- Keep the strongest achievement, supported metric, and differentiating technical mechanism.
- Never change a number, technology, scope, outcome, ownership level, or causal relationship to make text fit.
- Do not convert an estimate into a measured result or drop a qualifier that protects accuracy.

## Compression order

When shortening, remove or tighten content in this order:

1. filler and self-evident qualifiers;
2. duplicated context already clear from the role, project heading, or another bullet;
3. verbose connecting phrases and articles;
4. lower-value implementation detail;
5. secondary collaboration or process context.

Prefer precise substitutions such as “using” for “by leveraging” when meaning is unchanged. Do not sacrifice the primary result or mechanism merely to retain a fashionable verb.

## Expansion order

When a bullet needs more visual weight, add only supported detail in this order:

1. measured result or baseline;
2. technical mechanism;
3. system or data scale;
4. engineering constraint such as reliability or security;
5. concise ownership or collaboration context.

Never add filler, duplicate another bullet, or invent context to approach a target length.
When current wording lacks enough detail, use only explicit user facts or context files the user authorised the skill to read. A visually sparse but truthful draft is preferable to an unsupported full-looking one.

## Layout modes

- `one-line`: hard maximum 112 visible characters, with a preferred range of 105–112 only when the content supports it.
- `preserve-lines`: preserve a current one- or two-line footprint; compress any bullet currently exceeding two lines to two.
- `n-lines`: accept only one or two as the requested line count; reject larger values.
- `balanced-lines`: create a controlled ragged-right silhouette across the block. Use supplied examples as a rhythm reference; otherwise prefer mostly two-line bullets whose final lines end at naturally varied positions.
- `page-fit`: shorten the lowest-value wording first while preserving the number and substance of achievements.
- Bold spans are wider than surrounding text in many fonts. Re-render after fitting a bolded bullet; character count alone is insufficient.
- Every mode has a hard maximum of two rendered lines per bullet. A three-line bullet always fails verification and must never be applied.

## Rendered balance and visual roundness

- Measure visual footprint from the compiled LaTeX output or a supplied screenshot, not from raw or visible character count. Proportional glyph widths and word-boundary wrapping make equally long strings occupy different space.
- Judge `balanced-lines` at block level. Aim for a rounded, ragged-right edge: first and intermediate lines usually fill most of the measure, while final lines taper to different natural endpoints.
- Use two rendered lines for most bullets. Keep a complete one-line bullet when it is genuinely strong and concise; use one-line bullets sparingly and prefer them near the end of a block when that creates a clean taper.
- Never allow a third rendered line. If the supported result and mechanism cannot fit within two lines after three careful revisions, report the content conflict instead of dropping a material fact or applying the draft.
- Treat roughly 35–90% final-line fill as a useful visual range, not a hard quota. A shorter ending can look intentional when it contains a complete phrase; avoid orphaned words or fragments below roughly 25% when supported rewording can fix them.
- For a block containing at least three two-line bullets, require approximately 60% or greater average final-line fill and at least one fuller final line around 75% or greater. This is a block-density floor: individual shorter endings remain desirable for contrast.
- Fail `balanced-lines` when every ending clusters in the short range or when the block average remains below the density floor. Seek authorised evidence before expanding; if none supports useful detail, report the conflict and do not apply the draft.
- Preserve contrast: include both shorter and fuller endings when the content permits, and avoid making several bullets terminate at nearly the same horizontal position.
- A slightly shorter final bullet often closes a block cleanly, but do not force the section into a descending staircase or mechanical short–long alternation.
- Keep ordinary interword spacing and let LaTeX wrap naturally. Never insert manual line breaks, repeated spaces, non-breaking spaces, or horizontal-spacing commands merely to sculpt the silhouette.
- Preserve the template's font, margins, indentation, bullet spacing, and hanging indent; fitting this mode changes bullet wording only.
- Do not force every bullet to an identical width. Controlled variation is preferable to filler, weakened claims, or lost meaning.
- Character ceilings remain safety constraints, not proof of visual balance. A bullet cannot pass `balanced-lines` solely because its character count resembles the reference.

## Style and LaTeX

- Use concise British English and a strong, accurate opening verb.
- Keep one logical achievement per `\resumeItem`.
- Preserve meaningful punctuation when it improves scanability.
- Escape LaTeX-sensitive characters and ignore formatting commands when counting visible characters.
