# markdown-word-token-counter

A small Python script to count the **words** and **OpenAI-compatible tokens** in a Markdown file.

## First-time setup

1. Clone the repo and open it in **VS Code**.
2. Open the **integrated terminal** in VS Code.
3. Create and activate the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

4. Install the dependency:

```bash
python3 -m pip install -r requirements.txt
```

## Using it later

Each time you want to use the script:

1. Open the repo folder in **VS Code**
2. Open the **integrated terminal**
3. Activate the virtual environment:

```bash
source .venv/bin/activate
```

4. Run the script with the path to your Markdown file:

```bash
python3 count_tokens.py /path/to/your/file.md
```

You can also optionally provide a model name:

```bash
python3 count_tokens.py /path/to/your/file.md gpt-5
```

If no model name is provided, the script uses `gpt-5` by default.