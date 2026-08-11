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
- Rescan the selected target folder on every invocation, including follow-up revisions. Do not rely on a file listing, size, emptiness check, or extracted content from an earlier turn.
- If local inputs are missing, direct the user to `main.example.tex`, `job-description.example.txt`, and `cv-context.example/`. Do not edit the tracked examples with personal data.

## Validate the target

1. Normalize the target name only for directory matching, such as `Example Corp` to `example-corp`. Do not guess between multiple plausible folders.
2. Look for the target under `cv-context/experience/<target>/` and `cv-context/projects/<target>/`.
3. If exactly one matching folder exists, infer its target type. If neither exists, stop and report both expected paths. If both exist and the request does not identify the type, ask the user to choose.
4. Require the selected target folder to exist. Do not fall back to an example folder.
5. Recursively inventory every regular file in the selected folder before reading any evidence. For each file, record its relative path, extension, byte size, and one status: readable evidence, empty, hidden/metadata, unsupported, or unreadable.
6. Treat non-empty `.md`, `.txt`, and `.pdf` files as supported evidence. Read every supported file completely; do not stop after finding one strong source or assume similarly named files duplicate one another.
7. Re-check the inventory immediately before drafting. If a supported file was added, removed, or changed size during the task, read the current version and update the inventory before proceeding.
8. Exclude empty, hidden/metadata, unsupported, and unreadable files from factual evidence, but never omit them silently. List each excluded file and its reason in the final summary. Skip unreadable PDFs rather than inferring their contents.
9. Create a concise evidence map before drafting: summarise the useful facts contributed by each readable file and identify corroboration or conflicts across files. A file that contributes no selected bullet must still be analysed and recorded.
10. If the folder contains no readable, non-empty supported source, stop and report that no usable evidence exists. Prompt facts may supplement evidence but do not replace this folder requirement.
11. For experience, find the matching `\resumeSubheading` in `main.tex` and its immediately associated `\resumeItemListStart` block.
12. For a project, find the matching `\resumeProjectHeading` in `main.tex` and its immediately associated `\resumeItemListStart` block.
13. If the target block is missing or ambiguous, stop and report the problem.
14. Count the existing `\resumeItem{...}` entries in that block. Treat this count as immutable. If there are none, stop because the required output count is undefined.

## Build the bullets

1. Extract only supported facts: actions, technical implementation, scope, collaboration, outcomes, and evidenced metrics.
2. Accept additional facts supplied directly in the prompt as evidence for the current request. Do not save prompt facts into `cv-context/` unless explicitly asked.
3. Track the source file for each material claim while drafting. Cross-check every claim against the complete evidence map and flag material conflicts instead of choosing silently.
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

Summarize the target type and name edited; every file discovered and its status; useful evidence contributed by each readable file; excluded or unreadable files and reasons; bullet count preserved; rendered character count of each bullet; and whether PDF layout was visually verified. Mention any material prompt facts used. Do not claim that the CV guarantees an interview or acceptance.
