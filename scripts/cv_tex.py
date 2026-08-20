#!/usr/bin/env python3
"""Inspect LaTeX CV bullets without counting formatting commands as text."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Bullet:
    index: int
    line: int
    latex: str
    rendered: str
    characters: int


def strip_comments(source: str) -> str:
    """Remove unescaped LaTeX comments while preserving line numbers."""
    output: list[str] = []
    for line in source.splitlines(keepends=True):
        comment_at: int | None = None
        for index, char in enumerate(line):
            if char != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                comment_at = index
                break
        if comment_at is None:
            output.append(line)
        else:
            newline = "\n" if line.endswith("\n") else ""
            output.append(line[:comment_at] + newline)
    return "".join(output)


def mask_comments(source: str) -> str:
    """Mask unescaped LaTeX comments without changing source offsets."""
    output: list[str] = []
    for line in source.splitlines(keepends=True):
        comment_at: int | None = None
        for index, char in enumerate(line):
            if char == "%" and not _is_escaped(line, index):
                comment_at = index
                break
        if comment_at is None:
            output.append(line)
            continue

        content_end = len(line)
        if line.endswith("\r\n"):
            content_end -= 2
        elif line.endswith(("\n", "\r")):
            content_end -= 1
        output.append(
            line[:comment_at]
            + (" " * (content_end - comment_at))
            + line[content_end:]
        )
    return "".join(output)


def parse_braced(source: str, opening_brace: int) -> tuple[str, int]:
    depth = 0
    for cursor in range(opening_brace, len(source)):
        char = source[cursor]
        if char == "{" and not _is_escaped(source, cursor):
            depth += 1
        elif char == "}" and not _is_escaped(source, cursor):
            depth -= 1
            if depth == 0:
                return source[opening_brace + 1 : cursor], cursor + 1
    raise ValueError(f"Unclosed brace beginning at character {opening_brace}")


def _is_escaped(source: str, index: int) -> bool:
    backslashes = 0
    cursor = index - 1
    while cursor >= 0 and source[cursor] == "\\":
        backslashes += 1
        cursor -= 1
    return backslashes % 2 == 1


def rendered_text(latex: str) -> str:
    """Return a practical visible-text approximation for CV bullet prose."""
    escaped_dollar = "\ue000"
    text = latex.replace(r"\$", escaped_dollar)
    text = re.sub(
        r"\$\\sim\s*([^$]*)\$",
        lambda match: "~" + match.group(1).strip(),
        text,
    )
    replacements = {
        r"\%": "%",
        r"\&": "&",
        r"\_": "_",
        r"\#": "#",
        r"\{": "{",
        r"\}": "}",
        r"\textasciitilde": "~",
    }
    for latex_token, visible_token in replacements.items():
        text = text.replace(latex_token, visible_token)
    text = text.replace("$", "")
    text = text.replace(escaped_dollar, "$")
    text = re.sub(r"\\(?:textbf|textit|emph|textrm|texttt)\s*", "", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^]]*\])?", "", text)
    text = text.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", text).strip()


def extract_bullets(path: Path) -> list[Bullet]:
    source = strip_comments(path.read_text(encoding="utf-8"))
    document_at = source.find(r"\begin{document}")
    if document_at < 0:
        raise ValueError(f"{path} does not contain \\begin{{document}}")
    line_offset = source.count("\n", 0, document_at)
    source = source[document_at:]

    bullets: list[Bullet] = []
    pattern = re.compile(r"\\resumeItem\s*\{")
    cursor = 0
    while match := pattern.search(source, cursor):
        opening_brace = source.find("{", match.start())
        latex, cursor = parse_braced(source, opening_brace)
        visible = rendered_text(latex)
        line = line_offset + source.count("\n", 0, match.start()) + 1
        bullets.append(
            Bullet(
                index=len(bullets) + 1,
                line=line,
                latex=latex,
                rendered=visible,
                characters=len(visible),
            )
        )
    return bullets


def report_text(path: Path, bullets: list[Bullet]) -> None:
    print(f"{path}: {len(bullets)} bullets")
    for bullet in bullets:
        print(
            f"{bullet.index:>2}  line {bullet.line:>3}  "
            f"{bullet.characters:>3} chars  {bullet.rendered}"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("cv", type=Path, help="LaTeX CV to inspect")
    parser.add_argument("--compare", type=Path, help="Baseline CV for ordinal comparison")
    parser.add_argument("--max-chars", type=int, help="Fail when a bullet exceeds this limit")
    parser.add_argument(
        "--tolerance",
        type=int,
        help="With --compare, fail when a character-count delta exceeds this value",
    )
    parser.add_argument(
        "--require-same-text",
        action="store_true",
        help="With --compare, fail when visible bullet text changes",
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    try:
        bullets = extract_bullets(args.cv)
        baseline = extract_bullets(args.compare) if args.compare else None
    except (OSError, UnicodeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    failed = False
    comparisons: list[dict[str, object]] = []
    if args.max_chars is not None:
        failed |= any(bullet.characters > args.max_chars for bullet in bullets)

    if baseline is not None:
        if len(baseline) != len(bullets):
            print(
                f"error: bullet count changed from {len(baseline)} to {len(bullets)}",
                file=sys.stderr,
            )
            failed = True
        for before, after in zip(baseline, bullets):
            delta = after.characters - before.characters
            same_text = before.rendered == after.rendered
            comparisons.append(
                {
                    "index": after.index,
                    "before_characters": before.characters,
                    "after_characters": after.characters,
                    "delta": delta,
                    "same_text": same_text,
                }
            )
            if args.tolerance is not None and abs(delta) > args.tolerance:
                failed = True
            if args.require_same_text and not same_text:
                failed = True

    if args.json:
        print(
            json.dumps(
                {
                    "cv": str(args.cv),
                    "bullets": [asdict(bullet) for bullet in bullets],
                    "comparisons": comparisons,
                    "passed": not failed,
                },
                indent=2,
            )
        )
    else:
        report_text(args.cv, bullets)
        for comparison in comparisons:
            print(
                "compare "
                f"{comparison['index']:>2}: {comparison['delta']:+} chars, "
                f"same visible text={comparison['same_text']}"
            )

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
