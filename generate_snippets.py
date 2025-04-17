import os
import json

SNIPPET_DIR = "snippets_src"
OUTPUT_FILE = "outputs/vscode.code-snippets"

def load_snippet(filepath):
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    return lines

def generate_snippets():
    snippets = {}
    for file in os.listdir(SNIPPET_DIR):
        if file.endswith(".py"):
            name = file.replace(".py", "")
            path = os.path.join(SNIPPET_DIR, file)
            snippets[name] = {
                "prefix": name,
                "body": load_snippet(path),
                "description": f"Snippet auto-généré depuis {file}"
            }
    os.makedirs("outputs", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(snippets, f, indent=4)

if __name__ == "__main__":
    generate_snippets()
    print(f"✅ Snippets générés dans : {OUTPUT_FILE}")
