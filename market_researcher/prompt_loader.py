from pathlib import Path

_DIR = Path(__file__).parent / "prompts"

def load_prompt(name: str) -> str:
    path = _DIR / f"{name}.md"
    if not path.exists():
        return f"(TODO: write the methodology prompt for {name})"
    return path.read_text(encoding="utf-8")