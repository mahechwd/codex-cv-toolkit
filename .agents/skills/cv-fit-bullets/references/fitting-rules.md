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

## Layout modes

- `one-line`: hard maximum 112 visible characters, with a preferred range of 105–112 only when the content supports it.
- `preserve-lines`: actual rendered line count takes priority over character equality.
- `n-lines`: use the requested line count; there is no universal character limit for multi-line bullets.
- `balanced-lines`: keep comparable bullets at the intended common rendered line count and balance their final-line fill. Use an explicitly approved bullet as the visual reference; otherwise aim for each multi-line bullet's final line to occupy 70–90% of the available text width.
- `page-fit`: shorten the lowest-value wording first while preserving the number and substance of achievements.
- Bold spans are wider than surrounding text in many fonts. Re-render after fitting a bolded bullet; character count alone is insufficient.

## Rendered balance

- Measure visual footprint from the compiled LaTeX output or a supplied screenshot, not from raw or visible character count. Proportional glyph widths and word-boundary wrapping make equally long strings occupy different space.
- For `balanced-lines`, first match the reference or intended rendered line count. Then compare the final line's occupied width with the available bullet text width.
- When the user identifies an ideal reference bullet, prefer a final-line fill within approximately 10 percentage points of that reference over the generic 70–90% range.
- Avoid a dangling final line below roughly 60% fill when supported wording can rebalance it without changing the primary accomplishment.
- Do not force every bullet to an identical width. Consistent line count and broadly similar final-line fill are the goal; natural variation is preferable to filler or lost meaning.
- Character ceilings remain safety constraints, not proof of visual balance. A bullet cannot pass `balanced-lines` solely because its character count resembles the reference.

## Style and LaTeX

- Use concise British English and a strong, accurate opening verb.
- Keep one logical achievement per `\resumeItem`.
- Preserve meaningful punctuation when it improves scanability.
- Escape LaTeX-sensitive characters and ignore formatting commands when counting visible characters.
