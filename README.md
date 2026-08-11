# Codex CV Toolkit

A privacy-conscious LaTeX CV workspace for using Codex to turn raw evidence into concise, evidence-backed software-engineering CV bullets.

The repository contains a CV template and a repository-scoped Codex skill. Your personal CV, job descriptions, and supporting evidence stay in ignored local files, so they are not committed accidentally.

## What is included

```text
.
├── .agents/skills/
│   ├── build-cv-bullets/       # Working skill for creating CV bullets
│   └── tailor-cv-bullets/      # Reserved scaffold; not implemented yet
├── cv-context.example/
│   ├── experience/
│   └── projects/
├── job-description.example.txt
└── main.example.tex
```

After setup, your private working files will be:

```text
cv-context/                     # Notes, text files, and PDFs used as evidence
job-description.txt             # Vacancy text for future tailoring workflows
main.tex                        # Your editable CV
```

These paths are excluded by `.gitignore`.

## Prerequisites

- Git
- The ChatGPT desktop app with Codex, Codex CLI, or the Codex IDE extension
- A LaTeX distribution if you want to compile and visually verify the CV

Common LaTeX options include MacTeX or BasicTeX on macOS and TeX Live on Linux. The template uses `pdflatex` and the packages declared near the top of `main.tex`.

## Setup

1. Clone the repository and enter it:

   ```bash
   git clone <repository-url>
   cd codex-cv-toolkit
   ```

2. Create your private working files from the tracked examples:

   ```bash
   cp main.example.tex main.tex
   cp job-description.example.txt job-description.txt
   cp -R cv-context.example cv-context
   ```

3. Edit `main.tex` with your contact details, education, roles, projects, dates, and technologies. For every role or project that Codex should populate, add the required number of empty bullet entries:

   ```tex
   \resumeItemListStart
       \resumeItem{}
       \resumeItem{}
       \resumeItem{}
       \resumeItem{}
   \resumeItemListEnd
   ```

   The skill preserves this bullet count; it does not add or remove entries.

4. Add evidence for each target using a lowercase, hyphenated folder name:

   ```text
   cv-context/experience/example-company/
   cv-context/projects/example-project/
   ```

   Put one or more non-empty `.md`, `.txt`, or `.pdf` files in the target folder. Useful evidence includes:

   - work logs and project notes;
   - technical decisions and implementation details;
   - technologies used;
   - measurable outcomes, scale, reliability, or performance data;
   - collaboration and ownership details.

   Do not include credentials or confidential details that should not appear on a CV.

5. Open the repository root in Codex. In the desktop app, choose **Open folder**; in the CLI or IDE extension, start Codex with this repository as the working directory.

   Codex automatically discovers repository skills under `.agents/skills`. If the skill does not appear after an update, restart Codex.

## Build CV bullets

Explicitly invoke the skill and name exactly one experience or project. For example:

```text
Use $build-cv-bullets to build the bullets for Example Company.
```

You can also add facts directly in the prompt:

```text
Use $build-cv-bullets to build the bullets for Example Project.
Additional fact: I reduced the median API response time from 420 ms to 260 ms.
```

In the ChatGPT desktop app, you can select a skill with `@`. In Codex CLI or the IDE extension, use `/skills` or type `$` to mention it.

The skill will:

1. find the matching folder under `cv-context/experience/` or `cv-context/projects/`;
2. read all supported evidence files in that folder;
3. locate the matching entry in `main.tex`;
4. replace only that entry's existing bullets;
5. preserve the bullet count and surrounding LaTeX;
6. keep claims evidence-backed, escape LaTeX-sensitive characters, and enforce the configured length limit;
7. compile and inspect the result when a LaTeX toolchain is available.

The target name must be unambiguous and must already exist both in `main.tex` and in the corresponding context folder.

## Compile the CV

From the repository root, run:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Run it a second time if links or references need refreshing:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

This creates `main.pdf`. Review the PDF for line wrapping, spacing, page overflow, and visual balance before using it.

If `latexmk` is installed, you can instead use:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

## Job-description tailoring

`job-description.txt` and the `tailor-cv-bullets` directory are present for a future tailoring workflow. The tailoring skill files are currently empty, so `$tailor-cv-bullets` is not usable yet. Do not rely on it until its `SKILL.md` and rules have been implemented.

## Privacy and Git safety

Before every commit, check what Git will include:

```bash
git status --short
git diff --cached
```

The default `.gitignore` excludes `cv-context/`, `main.tex`, `cv_main.tex`, and `job-description.txt`. Keep reusable, anonymised starter content in the tracked `*.example.*` files and `cv-context.example/`; keep personal or employer-specific material only in the ignored working copies.

To confirm that a private path is ignored:

```bash
git check-ignore -v main.tex job-description.txt cv-context/
```

## Troubleshooting

- **The skill is missing:** open the repository root rather than a parent folder, then restart Codex.
- **No usable evidence found:** add at least one readable, non-empty `.md`, `.txt`, or `.pdf` file to the target folder.
- **Target not found:** make the company or project name in `main.tex` match the requested target and its context folder unambiguously.
- **Bullet count is undefined:** add one or more `\resumeItem{}` entries to the target block before invoking the skill.
- **PDF compilation fails:** inspect the first LaTeX error, confirm the required packages are installed, and ensure literal `%`, `&`, `_`, `#`, and `$` characters are escaped.
- **PDF was not visually checked:** install a LaTeX distribution, compile `main.tex`, and inspect `main.pdf` manually.

## Further reading

- [Official OpenAI documentation: ChatGPT desktop app](https://learn.chatgpt.com/docs/app)
- [Official OpenAI documentation: build and use skills](https://learn.chatgpt.com/docs/build-skills)
