---
name: cv-fit-bullets
description: Draft compressed, expanded, or visually balanced wording for one named LaTeX CV bullet block to meet a one-line, multi-line, balanced-line, or page footprint without changing facts. Produces a preview and may apply its own exact draft when explicitly requested.
---

# CV fit bullets

Fit selected bullets to the requested rendered space while preserving their strongest meaning.

## Establish the target

- Identify the exact CV path, kind (`experience` or `project`), and target name. Run `python3 scripts/cv_drafts.py list <cv-path>` and require one exact target.
- Read [references/fitting-rules.md](references/fitting-rules.md) completely before editing.
- Determine the requested mode:
  - `one-line`: each selected bullet must render on one line;
  - `preserve-lines`: retain each selected bullet's current rendered line count;
  - `n-lines`: fit each selected bullet to a user-specified line count;
  - `balanced-lines`: give comparable bullets a consistent rendered line count and similar final-line fill, using a visually approved bullet as the reference when supplied; or
  - `page-fit`: keep the whole CV within its existing page limit.
- When the user says “around 112 characters” or “one line” without another limit, use `one-line` with a hard ceiling of 112 visible characters.

## Capture the baseline and draft

1. Initialise a non-overwriting draft with `python3 scripts/cv_drafts.py init --cv <cv-path> --kind <kind> --target <name> --output drafts/fit/<descriptive-name>.json`.
2. Use its existing bullets, active count, and visible character counts as the baseline.
3. When a current PDF exists or LaTeX can compile, record the actual line count of every selected bullet and the total page count before drafting. For `balanced-lines`, also record each final line's approximate share of the available text width.
4. Preserve every factual element that materially supports the achievement: result, metric, mechanism, technology, scale, and ownership. Mark secondary context as compressible rather than silently dropping it.

## Fit the wording

1. Apply the requested mode and every rule in `references/fitting-rules.md`.
2. Write inner LaTeX strings only to the draft's `proposed_bullets`; do not edit the CV.
3. Do not add facts, job-description keywords, new metrics, or stronger ownership.
4. Preserve bullet count and order. Keep draft status as `draft`.
5. For `one-line`, target 105–112 visible characters when supported content fills that space naturally; accept a shorter bullet rather than padding it.
6. For `balanced-lines`, use the approved reference bullet's rendered line count and final-line fill as the target. Without a reference, use the block's intended common line count and aim for the final line of each multi-line bullet to occupy 70–90% of the available width.
7. Expand a visually short bullet only with supported result, mechanism, scale, constraint, or ownership detail. Never add filler or distort an XYZ claim to improve symmetry.

## Verify

- Run `python3 scripts/cv_drafts.py show <draft-path>` after drafting.
- Create `drafts/previews/<descriptive-name>.tex` with `python3 scripts/cv_drafts.py preview --cv <cv-path> --draft <draft-path> --output <preview-path>`. Run `python3 scripts/cv_tex.py` against the preview; for `one-line`, also pass `--max-chars 112`.
- Compile and inspect the preview PDF when possible. Verify the requested line count for every selected bullet and the page limit for `page-fit`. For `balanced-lines`, verify final-line fill visually or from rendered glyph positions; character count alone cannot pass this mode.
- If a selected bullet wraps incorrectly, revise that bullet and verify again. Stop after three unsuccessful visual fitting attempts and report which constraint conflicts with the content.
- When rendering is unavailable, compare against a supplied screenshot or visually approved neighbouring bullets and use visible character counts only as a fallback. Mark `balanced-lines` as estimated rather than verified.

## Report

List the draft and preview paths, CV path, target, mode, proposed changes, before/after visible character counts, facts deliberately preserved, facts removed as redundant context, final rendered line counts when verified, approximate final-line fill for `balanced-lines`, and page count when relevant. If the user explicitly asks this skill to apply that exact draft, show it once, set its status to `approved`, and run `python3 scripts/cv_drafts.py apply`; do not require another skill.
