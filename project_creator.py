import os
from code_generator import generate_file
from architecture_agent import llm as architect_llm
from code_generator import generate_file


project_name = input("Project Name: ")
project_type = input("Project Type: ")

# ARCHITECTURE

prompt = f"""
You are a software architect.

Design the file structure for:

{project_type}

Rules:
- Return only file paths
- One path per line
- No markdown
- No explanations

Example:

app.py
models.py
templates/index.html
static/style.css
README.md
"""

response = architect_llm.invoke(prompt)

files = []

for line in response.content.splitlines():

    line = line.strip()

    if not line:
        continue

    if line == "...":
        continue

    if "#" in line:
        continue

    files.append(line)
print("\nArchitecture:\n")

for f in files:
    print(f)

# CREATE PROJECT ROOT

os.makedirs(
    project_name,
    exist_ok=True
)

# CREATE FILES

for filepath in files:

    full_path = os.path.join(
        project_name,
        filepath
    )

    # If it's a directory

    if filepath.endswith("/"):

        os.makedirs(
            full_path,
            exist_ok=True
        )

        continue

    # If it's a file

    folder = os.path.dirname(
        full_path
    )

    if folder:

        os.makedirs(
            folder,
            exist_ok=True
        )
    code = generate_file(
        project_type,
        filepath
    )

    with open(
        full_path,
        "w"
    ) as f:

        f.write(code)
print("\nProject structure created.")
