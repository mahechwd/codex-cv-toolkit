# Repository instructions

## Privacy and evidence

- Treat `main.tex`, `job-description.txt`, and `cv-context/` as the user's actual private inputs. Never redirect them to the tracked `*.example.*` templates.
- Keep personal CVs, evidence, job descriptions, application copies, drafts, previews, and backups in the ignored paths documented in `README.md`.
- Never copy personal or employer-confidential material into tracked examples.
- Use only current bullet wording, the relevant `cv-context/` files, and explicit user facts as claim evidence. Never invent metrics, technologies, scale, ownership, outcomes, or causality.

## Bullet workflow

- Every bullet-writing request must identify one CV path, one kind (`experience` or `project`), and one exact target name from `python3 scripts/cv_drafts.py list <cv-path>`.
- Building, strengthening, fitting, tailoring, and bolding must produce or revise a JSON file under ignored `drafts/`. These stages must not edit a `.tex` CV.
- A request to generate or revise unseen wording is not approval to apply it. Show the resulting draft and wait for explicit approval of that exact file.
- Exact user-supplied bullets accompanied by an explicit request to apply them may be drafted and applied in the same task because the wording is already visible and approved.
- Apply approved bullet drafts only through `$cv-apply-bullets` and `python3 scripts/cv_drafts.py apply`. Never bypass the helper with a manual CV edit.
- The apply step may replace only the contents of existing `\resumeItem{...}` commands in the selected target. Preserve commands, bullet count, order, headings, dates, chronology, and every unrelated byte of the CV.
- Treat `main.tex` as canonical. Job-specific tailoring targets only a private `applications/<slug>/main.tex` copy.
- Scoring is read-only and must not modify the CV or draft.

## Verification

- Run `python3 -m unittest discover -s tests -v` after changing scripts.
- Run the official skill quick validator after changing any folder under `.agents/skills/`.
- When layout matters, validate a generated preview. State clearly when a LaTeX renderer is unavailable and line counts are estimated.
