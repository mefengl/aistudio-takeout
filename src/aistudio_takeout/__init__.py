#!/usr/bin/env python3
import sys, json, re
from pathlib import Path
from datetime import datetime


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ["-h", "--help"]:
        print(
            "aistudio-takeout - Convert Google AI Studio chats to Markdown\n\n"
            "Usage: aistudio-takeout <dir> [outdir]\n\n"
            "Output:\n"
            "  <outdir>/*.chat.md: Markdown files"
        )
        sys.exit(0)

    src = Path(sys.argv[1]).resolve()
    out = Path(sys.argv[2] if len(sys.argv) > 2 else "aistudio").resolve()

    if not src.exists():
        sys.exit(f"Error: {src} not found")
    if not src.is_dir():
        sys.exit(f"Error: {src} is not a directory")

    print(f"Converting {src.name}...")
    out.mkdir(exist_ok=True)

    files = [f for f in src.iterdir() if f.is_file() and not f.name.startswith(".")]
    n = 0

    for f in sorted(files):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue

        chunks = data.get("chunkedPrompt", {}).get("chunks", [])
        if not chunks:
            continue

        settings = data.get("runSettings", {})
        model = settings.get("model", "unknown").replace("models/", "")
        mtime = datetime.fromtimestamp(f.stat().st_mtime)
        created = mtime.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        date_prefix = mtime.strftime("%Y-%m-%d")

        title = f.stem
        md = [f"---\nprovider: aistudio\ncreated: {created}\nmodel: {model}\n---\n\n# {title}\n"]

        for chunk in chunks:
            role = chunk.get("role", "unknown")
            text = chunk.get("text", "")
            if not text and "parts" in chunk:
                text = chunk["parts"][0].get("text", "") if chunk["parts"] else ""
            md.append(f"\n## {'User' if role == 'user' else 'Model'}\n\n{text}\n")

        safe = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "-", title).strip("-") or "untitled"
        (out / f"{date_prefix}-{safe}.chat.md").write_text("".join(md), encoding="utf-8")
        n += 1
        print(f"✓ {date_prefix}-{safe}.chat.md")

    print(f"\nDone! {n} chats → {out}/")


if __name__ == "__main__":
    main()
