---
name: cv-apply-bullets
description: Apply one explicitly approved CV bullet draft to its named Experience or Projects target through the repository's guarded LaTeX helper. Use when the user approves or asks to apply a draft. Do not draft, rewrite, tailor, fit, bold, or score content.
---

# CV apply bullets

Apply a reviewed draft without changing any CV content outside the selected block's existing `\resumeItem{...}` bodies.

## Authorisation boundary

- Require the user to explicitly approve the exact draft in the current conversation or ask to apply a clearly named draft file.
- If approval is absent or the draft is not unambiguous, run `python3 scripts/cv_drafts.py show <draft-path>` and stop for approval without editing the CV or draft status.
- Read [references/draft-schema.md](references/draft-schema.md) completely before applying.
- Do not infer approval from the quality of a draft, an agent note, or the existence of the file.

## Review and apply

1. Run `python3 scripts/cv_drafts.py show <draft-path>` and report the recorded CV, target, status, and before/after bullets.
2. Confirm the draft identifies exactly one `experience` or `project` target and the intended CV path.
3. If the user has approved this exact draft and its status is `draft`, change only its top-level `status` value to `approved`.
4. Run `python3 scripts/cv_drafts.py apply --cv <cv-path> --draft <draft-path>`.
5. Never bypass the helper with a manual LaTeX edit. The helper enforces approval, target uniqueness, source fingerprint, bullet count, proposal safety, backup creation, and `\resumeItem`-content-only replacement.
6. Stop on any validation error. Create a fresh draft when the source block is stale; do not weaken or remove a guard.

## Report

State the applied draft, CV path, exact target, bullet count, backup path, and that surrounding LaTeX and unrelated content were preserved. Do not apply another draft unless it was also explicitly approved.
