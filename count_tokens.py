import sys
from pathlib import Path
import tiktoken


def count_words(text: str) -> int:
    return len(text.split())


def count_tokens(text: str, model_name: str = "gpt-4o") -> int:
    encoding = tiktoken.encoding_for_model(model_name)
    return len(encoding.encode(text))


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 count_tokens.py path/to/file.md")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: file not found: {file_path}")
        sys.exit(1)

    text = file_path.read_text(encoding="utf-8")

    words = count_words(text)
    tokens = count_tokens(text)

    print(f"File:   {file_path}")
    print(f"Words:  {words}")
    print(f"Tokens: {tokens}")


if __name__ == "__main__":
    main()