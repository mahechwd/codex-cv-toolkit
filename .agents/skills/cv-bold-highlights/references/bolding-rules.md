# LaTeX CV bolding rules

## What to emphasise

- Prefer a metric that communicates outcome or scale, such as `\textbf{30\%}`, `\textbf{10,000 listings}`, or `\textbf{3s latency}`.
- Prefer a technology or method only when it is central to how the result was achieved, such as `\textbf{Elasticsearch}` or `\textbf{Azure Kubernetes Service (AKS)}`.
- When a job description is in scope, prioritise supported terms relevant to its must-have work. Relevance never overrides truth.
- Select the shortest span that remains meaningful.

## Restraint

- Default to one bold span per bullet. Use a second only when it highlights a different category, normally one result and one mechanism.
- Leave a bullet unbolded when nothing is sufficiently distinctive.
- Do not bold an entire bullet, full clause, opening action verb, generic soft skill, company name, filler, punctuation, or every technology mentioned.
- Avoid consecutive bold spans that visually merge into a large block.
- Do not nest `\textbf{}` or combine new bolding with italics or underlining.

## Invariants

- Visible wording, punctuation, order, and whitespace-normalised text must remain identical before and after.
- Bold only existing, truthful content; do not introduce a keyword or metric.
- Keep LaTeX escapes inside the bold command.
- Re-render after formatting because bold glyphs can change line wrapping even when visible character count is unchanged.
- Preserve each selected bullet's original rendered line count and the CV's page count. Never leave a bullet above two rendered lines; remove lower-priority emphasis when needed.
- Direct edits may change only existing `\resumeItem{...}` contents in the selected block. Do not create draft or preview files.

## Guidance basis

- MIT career guidance recommends making relevant information immediately visible, quantifying outcomes, and using text emphasis sparingly.
- Oxford career guidance recommends consistent bold text as signposting and warns against overlong, hard-to-scan bullets.
