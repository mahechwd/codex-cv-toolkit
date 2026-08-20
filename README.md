# Codex CV Toolkit

A privacy-conscious, approval-gated toolkit for building and tailoring a LaTeX software-engineering CV with repository-scoped Codex skills.

The central rule is simple:

```text
evidence → draft JSON → human review → explicit approval → guarded LaTeX apply
```

Writing skills never edit a CV. `$cv-apply-bullets` is the only bullet-mutation workflow, and its deterministic helper replaces only the contents of existing `\resumeItem{...}` commands in one named Experience or Projects block.

## Start here: where your content goes

Run this once after cloning:

```bash
python3 scripts/setup_workspace.py
```

It creates the following ignored private inputs when they are missing and never overwrites files that already exist:

| Private input | What you put there |
|---|---|
| `main.tex` | Paste your complete LaTeX CV, including its existing Experience and Projects headings and `\resumeItem{...}` slots |
| `job-description.txt` | Paste one complete job description, replacing all previous placeholder or vacancy text |
| `cv-context/experience/<company-slug>/` | Add relevant `.md`, `.txt`, and `.pdf` evidence for that employment entry |
| `cv-context/projects/<project-slug>/` | Add relevant `.md`, `.txt`, and `.pdf` evidence for that project |

Then open the repository root in Codex and invoke the appropriate skill. For example:

```text
Use $cv-build-bullets on main.tex for experience "Example Company". Read its cv-context folder and create a draft only.
```

`main.example.tex`, `job-description.example.txt`, and `cv-context.example/` are tracked public templates used to initialise a new clone. Do not paste personal information into them, and do not delete them during normal use. Because they are tracked, deleting one correctly appears in Git as an uncommitted deletion. Restore an accidental deletion with:

```bash
git restore main.example.tex job-description.example.txt cv-context.example
```

New untracked files accidentally placed under `cv-context.example/` are ignored as a privacy backstop, but the correct location for all real evidence remains `cv-context/experience/<company-slug>/` or `cv-context/projects/<project-slug>/`.

If you already created `main.tex`, `job-description.txt`, or `cv-context/`, the setup command prints `kept existing` and leaves their contents untouched.

## What is included

| Skill | Purpose | Output |
|---|---|---|
| `$cv-build-bullets` | Fill empty slots or strengthen existing evidence-backed bullets without a default length limit | Draft JSON |
| `$cv-fit-bullets` | Compress or expand one block to a line-count or page footprint | Draft JSON + preview |
| `$cv-tailor-bullets` | Add only job-relevant terms supported by evidence | Draft JSON + preview |
| `$cv-bold-highlights` | Add sparse `\textbf{}` around existing metrics or technologies | Draft JSON + preview |
| `$cv-score` | Score ATS readiness and hiring-manager fit against a job description out of 100 | Read-only scorecard |
| `$cv-apply-bullets` | Apply one exact, explicitly approved draft | Selected CV block + backup |

There is intentionally no all-in-one `customise-cv` skill. Separating content, layout, job tailoring, formatting, scoring, and mutation makes each decision reviewable.

## Repository layout

```text
.
├── .agents/skills/          # Reusable repository-scoped workflows
├── AGENTS.md                # Repo-wide privacy and approval guardrails
├── scripts/
│   ├── cv_drafts.py         # Target discovery, draft, preview, guarded apply
│   ├── cv_tex.py            # Visible-text and bullet-count checks
│   ├── prepare_application.py
│   └── setup_workspace.py   # Non-destructive private-input setup
├── tests/
├── main.example.tex         # Public CV template
├── job-description.example.txt
└── cv-context.example/      # Public evidence templates
```

The following local working files are ignored by Git:

```text
main.tex
job-description.txt
cv-context/
applications/
drafts/
```

This keeps personal details, employer evidence, vacancies, application copies, draft prose, previews, and backups out of commits by default.

## Setup

Requirements are Python 3.10 or newer and Codex in the ChatGPT desktop app, CLI, or IDE extension. A LaTeX distribution is optional but required for true rendered line-count and page verification. Open the repository root so Codex discovers `AGENTS.md` and `.agents/skills/`.

Run from the repository root:

```bash
python3 scripts/setup_workspace.py
```

The initializer copies the tracked templates only when each private destination is missing. It deliberately has no overwrite option.

Paste or maintain your real CV only in `main.tex`. Keep one existing `\resumeItem{...}` command for every bullet slot you want the toolkit to manage. A slot may be empty:

```tex
\resumeItem{}
```

Paste the complete vacancy into `job-description.txt`. Do not put personal, confidential, vacancy, or employer-internal material in tracked examples.

## Add evidence

Create one folder per CV target:

```text
cv-context/experience/example-company/
cv-context/projects/example-project/
```

Folder names should be lowercase slugs of the company or project name in `main.tex`. Add non-empty `.md`, `.txt`, or `.pdf` sources with facts you can defend in an interview: contribution, mechanism, technology, scale, tests, reliability, security, performance, constraints, and outcomes.

The build skill rereads every supported file in the selected folder. Existing CV wording is useful evidence for rewording, but it never permits invented metrics, technologies, ownership, or impact.

## Select exactly what to edit

List the editable targets in a CV:

```bash
python3 scripts/cv_drafts.py list main.tex
```

Example output:

```text
experience: Example Company — Software Engineer (4 bullets)
project: Example Project — Technology Stack (4 bullets)
```

Every writing request should name:

- the CV path;
- `experience` or `project`; and
- the exact company or project name shown by `list`.

This prevents an agent from silently choosing the wrong section.

## Approval-gated workflow

### 1. Draft content

```text
Use $cv-build-bullets on main.tex for experience "Example Company". Read its cv-context folder. Fill empty slots or strengthen existing bullets, but create a draft only.
```

The skill creates an ignored file such as:

```text
drafts/build/example-company.json
```

It preserves the active slot count and records the current block fingerprint, existing bullets, proposed bullets, and evidence paths.

### 2. Review the proposal

```bash
python3 scripts/cv_drafts.py show drafts/build/example-company.json
```

Ask for revisions through the producing skill until the proposed bullets are right. The source CV remains unchanged.

To inspect a complete temporary TeX document before approval:

```bash
python3 scripts/cv_drafts.py preview \
  --cv main.tex \
  --draft drafts/build/example-company.json \
  --output drafts/previews/example-company.tex
```

### 3. Approve and apply

Approval must identify the exact draft:

```text
I approve drafts/build/example-company.json. Use $cv-apply-bullets to apply it.
```

The apply workflow changes the draft status to `approved`, then runs:

```bash
python3 scripts/cv_drafts.py apply \
  --cv main.tex \
  --draft drafts/build/example-company.json
```

The helper refuses to apply when:

- the draft is not approved;
- the Experience or Projects target is missing or ambiguous;
- the selected source block changed after drafting;
- the bullet count changed;
- a proposal is empty or contains a structural CV command;
- braces are unbalanced or `%` is unescaped; or
- the recorded CV path does not match the requested CV.

Before the atomic write, it creates a recovery copy under `drafts/backups/`. Only the inner byte ranges of the selected block's existing `\resumeItem{...}` commands are replaced.

## Fitting bullets

Content-first bullets may intentionally span multiple lines. Fit one named block only after its content is strong:

```text
Use $cv-fit-bullets on main.tex for experience "Example Company". Draft one-line versions with a hard maximum of 112 visible characters.
```

Supported modes are:

- `one-line`: default hard ceiling of 112 visible characters;
- `preserve-lines`: keep each bullet's rendered line count;
- `n-lines`: target a user-specified number of lines; and
- `page-fit`: keep the CV within its current page limit.

The skill creates a new draft and preview. Character count is only a fallback: proportional fonts and `\textbf{}` can change actual wrapping, so compile and inspect the preview whenever a LaTeX toolchain is available.

## Tailoring to a job

Paste one complete vacancy into ignored `job-description.txt`, then score the canonical CV:

```text
Use $cv-score to score main.tex against job-description.txt.
```

Create a non-overwriting private application workspace:

```bash
python3 scripts/prepare_application.py example-company-software-engineer
```

This creates:

```text
applications/example-company-software-engineer/
├── main.source.tex       # Immutable starting snapshot
├── main.tex              # Application working CV
└── job-description.txt
```

Tailor one named block at a time:

```text
Use $cv-tailor-bullets on applications/example-company-software-engineer/main.tex for experience "Example Company" against its job description. Create a draft only.
```

Supported equivalents and keywords may be proposed only when the relevant evidence or established bullet supports the same claim. Unsupported requirements remain honest gaps. Apply each approved draft separately, then rescore with the same `$cv-score` rubric.

## Sparse bold highlights

```text
Use $cv-bold-highlights on applications/example-company-software-engineer/main.tex for experience "Example Company". Create a draft only.
```

This stage may propose forms such as `\textbf{30\%}` or `\textbf{Elasticsearch}` while keeping visible wording identical. It defaults to one meaningful bold span per bullet and leaves low-signal bullets unbolded. Apply only after reviewing the preview because bold glyphs can change wrapping.

## Deterministic checks

Inspect active bullets and visible character counts:

```bash
python3 scripts/cv_tex.py main.tex
```

Enforce a 112-character ceiling:

```bash
python3 scripts/cv_tex.py drafts/previews/example-company.tex --max-chars 112
```

Compare visible text or character footprints:

```bash
python3 scripts/cv_tex.py drafts/previews/example-company.tex \
  --compare main.tex \
  --tolerance 3
```

Run the standard-library tests:

```bash
python3 -m unittest discover -s tests -v
```

## Compile and inspect

When a LaTeX toolchain is installed:

```bash
pdflatex -interaction=nonstopmode -halt-on-error \
  -output-directory=drafts/previews drafts/previews/example-company.tex
pdflatex -interaction=nonstopmode -halt-on-error \
  -output-directory=drafts/previews drafts/previews/example-company.tex
```

Inspect the PDF for line wrapping, page count, spacing, and machine-readable text before applying the draft.

## Truth policy

- Valid sources are current bullet wording, the relevant `cv-context/` folder, and explicit user facts.
- A skills-section keyword alone does not prove use in a specific achievement.
- Unsupported job requirements are reported gaps, not text to insert.
- Never invent metrics, scale, technologies, ownership, business impact, or causality.
- Preserve qualifiers such as “estimated” whenever accuracy depends on them.

## Privacy check before committing

```bash
git status --short
git diff --cached
git check-ignore -v main.tex job-description.txt cv-context/ applications/ drafts/
```

Only anonymised templates, reusable skills, scripts, and tests belong in Git.

## Further reading

- [Official OpenAI documentation: build skills](https://learn.chatgpt.com/docs/build-skills)
- [Google resume-writing guidance](https://services.google.com/fh/files/misc/resume-writing-tips-for-veterans-2021.pdf)
- [MIT guidance on skills, metrics, and concise bullets](https://capd.mit.edu/resources/resumes-writing-about-your-skills/)
- [Oxford University CV guidance](https://www.careers.ox.ac.uk/cvs)
