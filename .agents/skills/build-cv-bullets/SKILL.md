---
name: build-cv-bullets
description: Build polished software-engineering CV bullet points from raw employer evidence in cv-context and facts supplied in the prompt, then replace the corresponding empty or existing bullets in cv_main.tex. Use for creating bullets from notes, text files, PDFs, or an unstructured experience dump. Do not use for tailoring established bullets to a job description; use tailor-cv-bullets instead.
---

# Build CV bullets

Create evidence-backed bullets for one employer and write them directly into `cv_main.tex`.

## Required inputs

- Obtain the target employer from the request. Ask for it if it is unclear.
- Locate `cv_main.tex` and `cv-context/` from the repository root.
- Read [references/building-rules.md](references/building-rules.md) completely before drafting.

## Validate the target

1. Normalize the employer name only for directory matching, such as `Example Corp` to `example-corp`. Do not guess between multiple plausible folders.
2. Require `cv-context/<employer>/` to exist. If it does not, stop and report the expected path.
3. Recursively enumerate `.md`, `.txt`, and `.pdf` files in that folder. Ignore hidden files, `.gitkeep`, zero-byte files, and unsupported formats.
4. Read every usable file. Skip unreadable PDFs and list them in the final summary.
5. If the folder contains no readable, non-empty supported source, stop and report that no usable evidence exists. Prompt facts may supplement evidence but do not replace this folder requirement.
6. Find the employer's `\resumeSubheading` in `cv_main.tex` and its immediately associated `\resumeItemListStart` block. If it is missing or ambiguous, stop and report the problem.
7. Count the existing `\resumeItem{...}` entries in that block. Treat this count as immutable. If there are none, stop because the required output count is undefined.

## Build the bullets

1. Extract only supported facts: actions, technical implementation, scope, collaboration, outcomes, and evidenced metrics.
2. Accept additional facts supplied directly in the prompt as evidence for the current request. Do not save prompt facts into `cv-context/` unless explicitly asked.
3. Track the source of each material claim while drafting. Flag material conflicts instead of choosing silently.
4. Select distinct evidence for exactly the required number of bullets.
5. Apply every rule in `references/building-rules.md`.
6. Escape generated text correctly for LaTeX.

## Edit safely

1. Replace only the contents of the target employer's existing `\resumeItem{...}` entries.
2. Do not change bullet count, commands, layout, headings, employer, title, dates, location, projects, skills, or any other CV content.
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

Summarize the employer edited, evidence files used, unreadable files skipped, bullet count preserved, rendered character count of each bullet, and whether PDF layout was visually verified. Mention any material prompt facts used. Do not claim that the CV guarantees an interview or acceptance.
