---
name: cv-bold-highlights
description: Draft sparse LaTeX textbf emphasis for one named CV bullet block's most important existing metrics and supported technologies without changing visible wording. Produces a preview and may apply its own exact draft when explicitly requested.
---

# CV bold highlights

Add restrained `\textbf{...}` emphasis while keeping the visible CV text identical.

## Select scope

- Identify the exact CV path, kind (`experience` or `project`), and target name. Run `python3 scripts/cv_drafts.py list <cv-path>` and require one exact target.
- Read [references/bolding-rules.md](references/bolding-rules.md) completely before editing.
- Initialise a non-overwriting draft with `python3 scripts/cv_drafts.py init` under `drafts/bold/` and use its existing bullets as the baseline.

## Choose highlights

1. Read each bullet as a recruiter scanning for outcome, scale, and technical fit.
2. Select the smallest meaningful span, prioritising:
   - a decision-relevant metric or measured outcome; then
   - one supported technology, framework, method, or system term central to the achievement.
3. Apply every rule in `references/bolding-rules.md`.
4. Do not change, add, remove, reorder, or re-punctuate visible wording.

## Edit and verify

1. Wrap selected spans only with `\textbf{...}` in `proposed_bullets` and retain required LaTeX escapes inside the command, such as `\textbf{30\%}`.
2. Keep bullet count and order unchanged, status as `draft`, and the source CV untouched.
3. Create a preview with `python3 scripts/cv_drafts.py preview`, then compare it with `python3 scripts/cv_tex.py <preview-path> --compare <cv-path> --require-same-text`. The check must pass.
4. Compile and inspect the preview PDF when possible. If bolding creates a new line wrap or page overflow, remove the lower-priority highlight from the draft rather than rewriting content.
5. If rendering is unavailable, report that visual line wrapping was not verified.

## Report

List the CV, target, draft, and preview paths; each proposed bold span and why it is scan-worthy; confirmation that visible wording and bullet count are unchanged; and visual-verification status. If the user explicitly asks this skill to apply that exact draft, show it once, set its status to `approved`, and run `python3 scripts/cv_drafts.py apply`; do not require another skill.
