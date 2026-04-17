#!/usr/bin/env python3
"""
Simple transcript reader for AP assessment JSON files.
Designed for students to run quickly in Codespaces.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()


def find_default_transcript() -> Path | None:
    """Return assessment.json if present, else newest assessment*.json in cwd."""
    cwd = Path.cwd()

    primary = cwd / "assessment.json"
    if primary.exists():
        return primary

    candidates = sorted(cwd.glob("assessment*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0] if candidates else None


def load_json(path: Path) -> dict:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        console.print(f"[bold red]File not found:[/bold red] {path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        console.print(f"[bold red]Invalid JSON:[/bold red] {path}")
        console.print(f"[yellow]{e}[/yellow]")
        sys.exit(1)


def format_timestamp(raw: str) -> str:
    if not raw:
        return "N/A"
    try:
        dt = datetime.fromisoformat(raw)
        return dt.strftime("%Y-%m-%d %I:%M:%S %p")
    except Exception:
        return raw


def print_header(data: dict, source_path: Path) -> None:
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column(style="bold cyan", justify="right")
    table.add_column()

    table.add_row("Transcript", str(source_path))
    table.add_row("Student", data.get("student_name", "N/A"))
    table.add_row("Code file", data.get("code_file", "N/A"))
    table.add_row("Language", str(data.get("language", "N/A")).upper())
    table.add_row("Timestamp", format_timestamp(data.get("timestamp", "")))
    table.add_row("Questions answered", str(data.get("questions_answered", "N/A")))
    table.add_row("Completed full", str(data.get("completed_full_assessment", "N/A")))

    if "average_response_time_seconds" in data:
        table.add_row("Avg response (sec)", str(data.get("average_response_time_seconds", "N/A")))

    if "slow_response_count" in data:
        table.add_row("Slow responses", str(data.get("slow_response_count", "N/A")))

    console.print(Panel(table, title="AP Assessment Transcript", border_style="blue"))


def print_feedback_summary(data: dict) -> None:
    summary = data.get("practice_feedback_summary")
    if summary:
        console.print(Panel(Markdown(summary), title="Practice Feedback Summary", border_style="green"))


def conversation_pairs(conversation: list[dict]) -> list[tuple[str, str]]:
    """Convert raw conversation into displayable role/content tuples."""
    result: list[tuple[str, str]] = []
    for msg in conversation:
        role = msg.get("role", "unknown")
        content = msg.get("content", "")
        result.append((role, content))
    return result


def print_conversation(data: dict, limit: int | None = None, hide_system: bool = True) -> None:
    conversation = data.get("conversation", [])
    if not conversation:
        console.print("[yellow]No conversation data found.[/yellow]")
        return

    items = conversation_pairs(conversation)
    if hide_system:
        items = [(r, c) for (r, c) in items if "[SYSTEM:" not in c]

    if limit is not None and limit > 0:
        items = items[:limit]

    console.print(Panel(Text(f"Messages shown: {len(items)}", style="bold"), title="Conversation", border_style="magenta"))

    for idx, (role, content) in enumerate(items, start=1):
        if role == "assistant":
            title = f"AI Coach #{idx}"
            border = "yellow"
        elif role == "user":
            title = f"Student #{idx}"
            border = "cyan"
        else:
            title = f"{role} #{idx}"
            border = "white"

        console.print(Panel(Markdown(content), title=title, border_style=border))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read and format AP assessment transcript JSON files."
    )
    parser.add_argument(
        "transcript",
        nargs="?",
        help="Path to transcript JSON. If omitted, uses assessment.json or newest assessment*.json in current folder."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Show only the first N messages."
    )
    parser.add_argument(
        "--show-system",
        action="store_true",
        help="Include internal [SYSTEM: ...] messages in output."
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.transcript:
        transcript_path = Path(args.transcript)
    else:
        default_path = find_default_transcript()
        if default_path is None:
            console.print("[bold red]No transcript found.[/bold red]")
            console.print("Put assessment.json in this folder or pass a file path.")
            sys.exit(1)
        transcript_path = default_path

    data = load_json(transcript_path)
    print_header(data, transcript_path)
    print_feedback_summary(data)
    print_conversation(data, limit=args.limit, hide_system=not args.show_system)


if __name__ == "__main__":
    main()
