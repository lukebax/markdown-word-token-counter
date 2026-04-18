import sys
from pathlib import Path
import tiktoken


def count_words(text: str) -> int:
    return len(text.split())


def count_tokens(text: str, model_name: str) -> int:
    try:
        encoding = tiktoken.encoding_for_model(model_name)
    except KeyError:
        print(f"Error: unknown model '{model_name}'")
        print("Try upgrading tiktoken:")
        print("  python3 -m pip install --upgrade tiktoken")
        sys.exit(1)

    return len(encoding.encode(text))


def main():
    if len(sys.argv) not in (2, 3):
        print("Usage: python3 count_tokens.py path/to/file.md [model_name]")
        print("Example: python3 count_tokens.py file.md gpt-5")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    model_name = sys.argv[2] if len(sys.argv) == 3 else "gpt-5"

    if not file_path.exists():
        print(f"Error: file not found: {file_path}")
        sys.exit(1)

    text = file_path.read_text(encoding="utf-8")

    words = count_words(text)
    tokens = count_tokens(text, model_name)

    print(f"File:   {file_path}")
    print(f"Model:  {model_name}")
    print(f"Words:  {words}")
    print(f"Tokens: {tokens}")


if __name__ == "__main__":
    main()