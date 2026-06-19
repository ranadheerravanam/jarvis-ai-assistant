from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

task = input("Project: ")
prompt = f"""
You are a senior software architect.

Design the file structure for:

{task}

Rules:
- Return ONLY complete file paths.
- Do NOT return directory names.
- One path per line.
- No explanations.
- No markdown.

Example:

app.py
models.py
database.py
routes.py
templates/index.html
templates/new.html
templates/edit.html
static/style.css
static/script.js
images/icon.png
fonts/font.ttf
requirements.txt
README.md
"""
response = llm.invoke(prompt)

print(response.content)
