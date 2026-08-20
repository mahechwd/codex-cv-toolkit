---
name: cv-build-bullets
description: Draft or strengthen content-first software-engineering CV bullets from pasted text, current CV bullets, explicit user facts, and optionally requested context. Use for prompt-only rewrites or one named Experience or Projects block without a default length limit. Do not read context files or PDFs unless explicitly requested. Produces chat proposals or review files and never edits a CV.
---

# CV build bullets

Create the strongest truthful bullets before layout compression. Work in either prompt-only mode or CV-targeted draft mode.

## Choose the mode

- Read [references/building-rules.md](references/building-rules.md) completely before drafting.
- Use **prompt-only mode** when the user pastes bullets and asks to create, edit, strengthen, or reword them without asking to target a CV file.
- Use **CV-targeted draft mode** when the request names, or clearly intends to update, a block in a CV file.
- Do not force a pasted-bullet request through repository discovery, `main.tex`, `cv-context/`, or the JSON draft workflow.

## Control context access

- By default, do not list, inspect, or read anything under `cv-context/`. Existing or pasted bullet wording and facts explicitly supplied in the prompt are valid evidence by themselves.
- If the user names one or more context files, read only those files.
- If the user explicitly asks to use a target's context folder, rescan that folder and read its non-empty `.md` and `.txt` files. Report empty, hidden, unsupported, or unreadable files without treating them as evidence.
- Do not open, extract, or summarise any PDF merely because it exists or because the user asked to use a context folder.
- Read a PDF only when the user explicitly asks to use/read PDFs or names that exact `.pdf` file. Read only the authorised PDF files and skip unreadable ones without inferring their contents.
- Do not make optional context a prerequisite. If the available bullets and prompt facts support the task, proceed without asking for files.
- If the user requests new bullets but provides no usable facts and the target has only empty slots, ask for facts or explicit permission to use named context; do not search for evidence automatically.

## Prompt-only mode

1. Treat the pasted bullets and explicit accompanying facts as the complete evidence set unless the user explicitly authorises context access.
2. Preserve the number of bullets unless the user requests a different count.
3. Strengthen the achievement, technical mechanism, and supported impact without adding unsupported facts.
4. If the pasted text contains `\resumeItem{...}` commands, change only their inner content and preserve the wrappers and surrounding text exactly.
5. Do not impose a character or line limit unless the user supplies one. Use `$cv-fit-bullets` later when layout is the actual goal.
6. Return the proposed bullets in chat in the same general format as the input. Do not create a JSON draft or edit any file unless the user asks to bind the result to a named CV target.

## CV-targeted draft mode

1. Obtain an explicit kind (`experience` or `project`), target name, and CV path; default to canonical `main.tex` only when that is clearly intended.
2. Run `python3 scripts/cv_drafts.py list <cv-path>` and require one exact target match. Do not guess between plausible targets.
3. Initialise a non-overwriting draft with `python3 scripts/cv_drafts.py init --cv <cv-path> --kind <kind> --target <name> --output drafts/build/<descriptive-name>.json`.
4. Use the recorded active `\resumeItem{...}` slots. Preserve their count. Stop if the block is missing, ambiguous, or contains no slots.
5. Treat non-empty current bullets and explicit prompt facts as sufficient evidence. Add context evidence only under the access rules above.
6. Do not edit tracked examples with personal information.

## Build the draft

1. If all existing slots are empty, create distinct achievements from the available evidence. If any contain text, strengthen or reword them using their established claims and any authorised evidence; retain strong wording that does not need change.
2. Select distinct, material achievements for exactly the available bullet slots.
3. Track the source of every claim, including technologies, metrics, ownership, scale, and outcomes.
4. Apply every content rule in `references/building-rules.md`.
5. Do not impose a character or line limit unless the user explicitly provides one. Preserve useful technical mechanism and context even when the first draft spans multiple lines.
6. Escape LaTeX-sensitive characters and write inner LaTeX only—never include `\resumeItem{}` wrappers.
7. Replace only `proposed_bullets`, `evidence_files`, and `notes` in the JSON draft. Keep `status` as `draft`; do not edit any `.tex` file.

## Verify and report

- Run `python3 scripts/cv_drafts.py show <draft-path>` and confirm the proposed count matches the recorded slots and every proposed bullet is non-empty.
- Re-read the proposals and trace each material claim to current wording, prompt facts, or an explicitly authorised context source.
- Report the draft path, target, evidence actually used, bullet count, rendered character counts, and any context files intentionally skipped. Do not imply that unrequested context was inspected.
- State explicitly that the bullets are content-first and have not been fitted to a page unless the user also requested and authorised that separate work.
- Ask the user to review the draft. Applying it is a separate `$cv-apply-bullets` action requiring explicit approval.
