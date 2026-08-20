# Content-first CV bullet rules

## Evidence and integrity

- Use only facts supported by pasted or current bullet wording, facts explicitly supplied by the user, or context sources the user explicitly authorised the skill to read.
- Treat optional context as corroboration or additional evidence, not as a mandatory input.
- Never invent or strengthen metrics, scale, ownership, technologies, outcomes, or business impact.
- Omit unsupported metrics; never insert placeholders such as `[X%]`.
- Resolve material conflicts before editing.
- Exclude credentials, personal information, internal identifiers, and confidential implementation details unsuitable for a public CV.

## Recruiter-readable technical credibility

- Start with an accurate action verb and use concise British English.
- Lead with the plain-English accomplishment, user or business value, or measurable engineering result. Put implementation detail after the reader understands why the work mattered.
- Make the opening clause understandable to a general recruiter without requiring them to decode the technology stack, architecture, or internal system vocabulary.
- Make the XYZ relationship explicit: state the accomplishment (X), include its measurement or scale (Y) when supported, and explain the technical method (Z).
- Prefer compact causal forms such as “Reduced X by Y by implementing Z” or “Built Z, enabling X at Y scale”. Do not force a metric or awkward sentence order when the evidence lacks Y.
- Lead with the most differentiating result or engineering contribution rather than a duty.
- Name only the one or two technologies, frameworks, algorithms, or architectural choices that best explain how the result was achieved. Do not turn a bullet into a stack inventory.
- Choose the smallest concrete technical detail that proves engineering credibility, such as a design decision, constraint, algorithm, scale characteristic, or reliability mechanism. Do not preserve every available implementation detail.
- Demonstrate senior-level depth through causality and judgement—why the method produced the result or handled a constraint—not through dense terminology.
- Replace internal names and niche jargon with their plain-English function. Use an acronym without expansion only when it is broadly recognised for the target role and genuinely improves the bullet.
- Avoid long chains of technical nouns, multiple parenthetical explanations, and lists of tools joined by commas.
- Give every bullet a distinct purpose and avoid repeated opening verbs, claims, metrics, and tool lists.
- Prefer clear technical language to grandiose or unusual verbs. Avoid first-person pronouns, vague praise, filler, keyword stuffing, and unverifiable adjectives such as “top 5%”.
- Metrics may quantify performance, scale, reliability, coverage, latency, cost, adoption, delivery, or accuracy. A bullet remains valid without a metric when its technical contribution is strong and evidence-backed.
- Give each bullet one main accomplishment and one causal chain. Do not combine two independently valuable achievements merely because they came from the same source sentence.
- Split separate achievements across available bullet slots when each has its own outcome, method, or evidence. Avoid joining them with “and” unless the second phrase directly completes the same mechanism or result.

## Two-audience test

- **HR scan:** after reading the opening clause, a non-technical recruiter can state what improved, what was delivered, or why the work mattered.
- **Senior SWE scan:** after reading the full bullet, an experienced engineer can identify a concrete method, engineering decision, constraint, or scale signal that makes the claim credible.
- If only the HR test passes, add one supported technical mechanism. If only the senior SWE test passes, simplify the opening and remove low-signal implementation detail.
- Prefer “Improved payment retrieval speed by 30% by redesigning Elasticsearch pagination” to a catalogue of service types, indexing internals, infrastructure, and query primitives.

## Length and focus

- Use a hard ceiling of 220 visible characters per bullet, including spaces and punctuation, unless the user explicitly supplies a different limit.
- Aim for a natural block average of 175–180 visible characters. Enforce 180 as the default maximum block average in CV edit mode; 175 is a soft target, not a minimum.
- Keep a strong bullet shorter when the complete supported XYZ claim needs fewer words. Never pad with extra technologies, adjectives, or context to approach the target.
- Allow a bullet to approach 220 only when the additional supported mechanism, constraint, scale, or outcome materially strengthens the same accomplishment.
- Before accepting a long bullet, remove repeated context and ask whether it contains two accomplishments that should occupy separate existing slots.
- Count rendered characters rather than LaTeX syntax: escaped forms such as `\%` and `\&` count as one visible character each, while commands such as `\textbf{}` contribute only their visible contents.
- In CV edit mode, do not rely on estimation: run the target-specific length check and revise until both the 220-character per-bullet ceiling and 180-character maximum block average pass.
- Use `$cv-fit-bullets` in a separate request when the user wants one-line bullets, an exact rendered line count, or a one-page CV.

## LaTeX

- In CV edit mode, change only the inner content of each existing `\resumeItem{...}` slot and preserve every wrapper and surrounding byte.
- In prompt-only mode, preserve any pasted `\resumeItem{...}` wrappers and modify only their inner text.
- Escape literal `%`, `&`, `_`, `#`, and `$` characters.
- Keep each replacement as one logical bullet and preserve the existing bullet count and order.

## Guidance basis

- Google recommends showing an accomplishment, a measurement when available, and how it was achieved.
- MIT career guidance recommends strong action verbs, relevant tasks, outcomes, metrics, and one-to-two-line final resume bullets. This skill deliberately handles the richer content-first draft before final fitting.
