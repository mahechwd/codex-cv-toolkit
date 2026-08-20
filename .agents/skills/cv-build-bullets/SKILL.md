---
name: cv-build-bullets
description: Draft content-first software-engineering CV bullets for one named Experience or Projects block from cv-context evidence and user facts. Use to fill empty bullet slots or strengthen existing bullets without a length limit. Produces a review file and never edits a CV.
---

# CV build bullets

Create the strongest truthful bullets for one experience or project before layout compression.

## Select the target

- Obtain an explicit kind (`experience` or `project`), target name, and CV path; default to canonical `main.tex` only when that is clearly intended.
- Run `python3 scripts/cv_drafts.py list <cv-path>` and require one exact target match.
- Locate the matching folder under `cv-context/experience/` or `cv-context/projects/`.
- Read [references/building-rules.md](references/building-rules.md) completely before drafting.
- Rescan the selected evidence folder on every invocation, including follow-up revisions.
- Do not edit tracked examples with personal information.

## Validate the target and evidence

1. Match the target to exactly one evidence folder of the selected kind. Do not guess between plausible folders.
2. Inventory every regular file recursively. Record its relative path, extension, byte size, and status: readable evidence, empty, hidden/metadata, unsupported, or unreadable.
3. Read every non-empty `.md`, `.txt`, and `.pdf` file completely. Never stop after finding one useful source or assume similar filenames are duplicates.
4. Recheck the inventory immediately before drafting. Read any supported file that was added or changed during the task.
5. Build a concise evidence map showing the useful facts contributed by each readable file and any conflicts.
6. Stop if there is no readable evidence. User-supplied prompt facts may supplement but do not replace the target folder.
7. Initialise a non-overwriting draft with `python3 scripts/cv_drafts.py init --cv <cv-path> --kind <kind> --target <name> --output drafts/build/<descriptive-name>.json`.
8. Use the recorded active `\resumeItem{...}` slots. Preserve their count. Stop if the block is missing, ambiguous, or contains no slots.

## Build the draft

1. If all existing slots are empty, create distinct achievements. If any contain text, strengthen or reword them using both their established claims and the evidence; retain strong wording that does not need change.
2. Select distinct, material achievements for exactly the available bullet slots.
3. Track the source of every claim, including technologies, metrics, ownership, scale, and outcomes.
4. Apply every content rule in `references/building-rules.md`.
5. Do not impose a character or line limit unless the user explicitly provides one. Preserve useful technical mechanism and context even when the first draft spans multiple lines.
6. Escape LaTeX-sensitive characters and write inner LaTeX only—never include `\resumeItem{}` wrappers.
7. Replace only `proposed_bullets`, `evidence_files`, and `notes` in the JSON draft. Keep `status` as `draft`; do not edit any `.tex` file.

## Verify and report

- Run `python3 scripts/cv_drafts.py show <draft-path>` and confirm the proposed count matches the recorded slots and every proposed bullet is non-empty.
- Re-read the proposals and trace each material claim to the evidence map.
- Report the draft path, target, every discovered evidence file and status, evidence used, bullet count, rendered character counts, and any prompt facts used.
- State explicitly that the bullets are content-first and have not been fitted to a page unless the user also requested and authorised that separate work.
- Ask the user to review the draft. Applying it is a separate `$cv-apply-bullets` action requiring explicit approval.
