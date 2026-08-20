---
name: cv-build-bullets
description: Write or strengthen concise, XYZ-style software-engineering CV bullets from pasted text, current CV bullets, explicit user facts, and optionally requested context. Use for prompt-only rewrites or to edit one named Experience or Projects block directly in a LaTeX CV. Defaults to a 220-visible-character ceiling. Do not read context files or PDFs unless explicitly requested.
---

# CV build bullets

Create the strongest truthful bullets before layout compression. Work in either prompt-only mode or CV edit mode.

## Choose the mode

- Read [references/building-rules.md](references/building-rules.md) completely before drafting.
- Use **prompt-only mode** when the user pastes bullets and asks to create, edit, strengthen, or reword them without asking to target a CV file.
- Use **CV edit mode** when the request names, or clearly intends to update, a block in a CV file.
- Do not force a pasted-bullet request through repository discovery, `main.tex`, or `cv-context/`.

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
5. Apply the default length rules below unless the user supplies a different limit. Use `$cv-fit-bullets` later when exact line wrapping or page layout is the actual goal.
6. Return the proposed bullets in chat in the same general format as the input. Do not edit a file unless the user asks to target a named CV block.

## CV edit mode

1. Obtain an explicit kind (`experience` or `project`), target name, and CV path; default to canonical `main.tex` only when that is clearly intended.
2. Run `python3 scripts/cv_drafts.py list <cv-path>` and require one exact target match. Do not guess between plausible targets.
3. Read the exact target block and record its active `\resumeItem{...}` contents and count. Stop if the block is missing, ambiguous, or contains no slots.
4. Treat non-empty current bullets and explicit prompt facts as sufficient evidence. Add context evidence only under the access rules above.
5. Build exactly one replacement for each existing slot, then use `apply_patch` to replace only the inner content of those `\resumeItem{...}` commands in the selected block.
6. Edit the named CV immediately. Do not create a draft JSON and do not wait for a separate approval step.
7. Do not add, delete, reorder, or move bullet commands. Preserve headings, roles, dates, locations, chronology, commands, comments, whitespace outside the selected inner contents, and every unrelated byte.
8. Never edit tracked examples with personal information.

## Write the bullets

1. If all existing slots are empty, create distinct achievements from the available evidence. If any contain text, strengthen or reword them using their established claims and any authorised evidence; retain strong wording that does not need change.
2. Decompose the evidence into atomic achievements before assigning it to slots. Each bullet should communicate one main outcome and one supporting technical method.
3. When one source bullet contains two independently valuable achievements, split them across two existing slots when the block has capacity. Reuse an empty, weak, or redundant slot; never add a new `\resumeItem` command.
4. Select distinct, material achievements for exactly the available bullet slots.
5. Track the source of every claim, including technologies, metrics, ownership, scale, and outcomes.
6. Apply every content and length rule in `references/building-rules.md`.
7. Escape LaTeX-sensitive characters correctly inside each existing wrapper.

## Verify and report

- Rerun `python3 scripts/cv_drafts.py list <cv-path>` and `python3 scripts/cv_tex.py <cv-path>` after editing.
- Confirm the selected bullet count is unchanged, every bullet is non-empty and at most 220 visible characters, the block average is normally near 170–180 characters, LaTeX is balanced, and no content outside the selected `\resumeItem{...}` bodies changed. Correct the edit immediately if any invariant fails.
- Recheck bullets near 220 characters for multiple achievements, repeated context, or detachable implementation detail. Split or tighten them when another existing slot can carry a distinct achievement.
- Re-read the final bullets and trace each material claim to current wording, prompt facts, or an explicitly authorised context source.
- Report the CV path, target, before/after bullets, evidence actually used, bullet count, rendered character counts, and any context files intentionally skipped. Do not imply that unrequested context was inspected.
- State explicitly that the bullets are content-first and have not been fitted to a page unless the user also requested and authorised that separate work.
- Tell the user that the named CV block has been updated and they can request another revision after reviewing `main.tex`.
