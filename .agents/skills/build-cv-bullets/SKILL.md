---
name: build-cv-bullets
description: Build polished software-engineering CV bullet points for work experience or projects from raw evidence in cv-context and facts supplied in the prompt, then replace the corresponding bullets in main.tex. Use for creating bullets from notes, text files, PDFs, or an unstructured experience dump. Do not use for tailoring established bullets to a job description; use tailor-cv-bullets instead.
---

# Build CV bullets

Create evidence-backed bullets for one experience or project and write them directly into `main.tex`.

## Required inputs

- Obtain the target name from the request. Ask for it if it is unclear.
- Locate `main.tex` and `cv-context/` from the repository root.
- Read [references/building-rules.md](references/building-rules.md) completely before drafting.
- If local inputs are missing, direct the user to `main.example.tex`, `job-description.example.txt`, and `cv-context.example/`. Do not edit the tracked examples with personal data.

## Validate the target

1. Normalize the target name only for directory matching, such as `Example Corp` to `example-corp`. Do not guess between multiple plausible folders.
2. Look for the target under `cv-context/experience/<target>/` and `cv-context/projects/<target>/`.
3. If exactly one matching folder exists, infer its target type. If neither exists, stop and report both expected paths. If both exist and the request does not identify the type, ask the user to choose.
4. Require the selected target folder to exist. Do not fall back to an example folder.
5. Recursively enumerate `.md`, `.txt`, and `.pdf` files in that folder. Ignore hidden files, `.gitkeep`, zero-byte files, and unsupported formats.
6. Read every usable file. Skip unreadable PDFs and list them in the final summary.
7. If the folder contains no readable, non-empty supported source, stop and report that no usable evidence exists. Prompt facts may supplement evidence but do not replace this folder requirement.
8. For experience, find the matching `\resumeSubheading` in `main.tex` and its immediately associated `\resumeItemListStart` block.
9. For a project, find the matching `\resumeProjectHeading` in `main.tex` and its immediately associated `\resumeItemListStart` block.
10. If the target block is missing or ambiguous, stop and report the problem.
11. Count the existing `\resumeItem{...}` entries in that block. Treat this count as immutable. If there are none, stop because the required output count is undefined.

## Build the bullets

1. Extract only supported facts: actions, technical implementation, scope, collaboration, outcomes, and evidenced metrics.
2. Accept additional facts supplied directly in the prompt as evidence for the current request. Do not save prompt facts into `cv-context/` unless explicitly asked.
3. Track the source of each material claim while drafting. Flag material conflicts instead of choosing silently.
4. Select distinct evidence for exactly the required number of bullets.
5. Apply every rule in `references/building-rules.md`.
6. Escape generated text correctly for LaTeX.

## Edit safely

1. Replace only the contents of the selected experience or project's existing `\resumeItem{...}` entries.
2. Do not change bullet count, commands, layout, headings, names, titles, dates, locations, technologies, skills, or any other CV content.
3. Re-read the edited block and verify:
   - the number of bullets is unchanged;
   - every claim is supported;
   - every rendered bullet is at most 113 characters;
   - bullets occupy a visually consistent amount of line space in the CV;
   - LaTeX-sensitive characters are escaped;
   - no bullet is empty.
4. When LaTeX rendering is available, compile and inspect the target block. Do not use character count alone as a proxy for visual width in a proportional font.
5. If rendering is unavailable, compare wording and likely visual width against adjacent bullets and report that visual PDF verification was not performed.
6. If verification fails, revise only the target bullets and verify again.

## Report

Summarize the target type and name edited, evidence files used, unreadable files skipped, bullet count preserved, rendered character count of each bullet, and whether PDF layout was visually verified. Mention any material prompt facts used. Do not claim that the CV guarantees an interview or acceptance.
