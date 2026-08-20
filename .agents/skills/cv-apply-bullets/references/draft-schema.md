# CV bullet draft contract

`scripts/cv_drafts.py init` creates the canonical JSON shape. Producers may change only `proposed_bullets`, `evidence_files`, and `notes` while drafting. The apply workflow may change `status` from `draft` to `approved` only after explicit user approval.

```json
{
  "schema_version": 1,
  "status": "draft",
  "cv_path": "main.tex",
  "target": {
    "kind": "experience",
    "name": "Example Company"
  },
  "baseline_fingerprint": "sha256:...",
  "expected_bullet_count": 4,
  "existing_bullets": [
    {
      "latex": "Existing bullet",
      "rendered": "Existing bullet",
      "characters": 15
    }
  ],
  "proposed_bullets": ["Proposed bullet"],
  "evidence_files": ["cv-context/experience/example-company/evidence.md"],
  "notes": []
}
```

## Status lifecycle

`draft` → `approved` → `applied`

- Producers must leave status as `draft`.
- Approval applies to one exact draft file, target, and proposed bullet list.
- The guarded helper marks a successful draft `applied` and records `applied_at` and `backup_path`.

## Mutation invariants

- One draft addresses exactly one named Experience or Projects block.
- The source block fingerprint and active bullet count must still match the draft.
- `proposed_bullets` contains one non-empty inner-LaTeX string per existing `\resumeItem` slot.
- Proposed strings must not include a `\resumeItem{...}` wrapper, structural CV commands, unbalanced braces, or unescaped `%`.
- Applying replaces only the byte ranges inside the target's existing `\resumeItem{...}` braces. It does not add, delete, reorder, or move bullet commands.
- A source backup is created under ignored `drafts/backups/` before the CV is replaced atomically.
