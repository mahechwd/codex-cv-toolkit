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
- `page-fit`: shorten the lowest-value wording first while preserving the number and substance of achievements.
- Bold spans are wider than surrounding text in many fonts. Re-render after fitting a bolded bullet; character count alone is insufficient.

## Style and LaTeX

- Use concise British English and a strong, accurate opening verb.
- Keep one logical achievement per `\resumeItem`.
- Preserve meaningful punctuation when it improves scanability.
- Escape LaTeX-sensitive characters and ignore formatting commands when counting visible characters.
