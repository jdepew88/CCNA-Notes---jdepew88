"""Convert all .docx files in CCNA Notes - Word Docs to markdown."""

from pathlib import Path

from markitdown import MarkItDown

REPO_ROOT = Path(__file__).resolve().parent.parent
WORD_DOCS = REPO_ROOT / "CCNA Notes - Word Docs"
MARKDOWN_DIR = REPO_ROOT / "CCNA Notes - markdown"


def main() -> None:
    MARKDOWN_DIR.mkdir(exist_ok=True)
    converter = MarkItDown()

    docx_files = sorted(
        f for f in WORD_DOCS.glob("*.docx") if not f.name.startswith("~$")
    )

    converted = 0
    failed: list[tuple[str, str]] = []

    for docx_path in docx_files:
        md_path = MARKDOWN_DIR / f"{docx_path.stem}.md"
        try:
            result = converter.convert(str(docx_path))
            md_path.write_text(result.text_content, encoding="utf-8")
            converted += 1
            print(f"OK  {docx_path.name} -> {md_path.name}")
        except Exception as exc:
            failed.append((docx_path.name, str(exc)))
            print(f"ERR {docx_path.name}: {exc}")

    print(f"\nConverted {converted}/{len(docx_files)} files to {MARKDOWN_DIR}")
    if failed:
        print("Failed:")
        for name, err in failed:
            print(f"  - {name}: {err}")


if __name__ == "__main__":
    main()
