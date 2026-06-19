from langchain_ollama import ChatOllama
from file_tools import create_folder, create_file
import re

llm = ChatOllama(model="llama3.2")

project_name = input("Project Name: ")
project_type = input("Project Type: ")

prompt = f"""
You are a senior software architect.

Create a complete {project_type} project.

Rules:

- Return files in this exact format:

FILENAME: app.py
<code>

FILENAME: README.md
<content>

FILENAME: requirements.txt
<content>

- No markdown fences.
- No explanations.
- Generate multiple files.
"""

response = llm.invoke(prompt)

content = response.content

create_folder(project_name)

parts = re.split(r"FILENAME:\s*", content)

for part in parts:

    part = part.strip()

    if not part:
        continue

    lines = part.splitlines()

    filename = lines[0].strip()

    file_content = "\n".join(lines[1:])
    file_content = file_content.replace(
        "```python",
        ""
    )

    file_content = file_content.replace(
        "```",
        ""
    )

    create_file(
        f"{project_name}/{filename}",
        file_content
    )

print("\nProject generated successfully.")
