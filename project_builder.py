from langchain_ollama import ChatOllama
from file_tools import create_folder, create_file

llm = ChatOllama(model="llama3.2")

project_name = input("Project Name: ")
project_type = input("Project Type: ")

prompt = f"""
You are a senior software engineer.

Create a complete {project_type} project.

Rules:
- Return ONLY Python code.
- No markdown.
- No explanations.
- Code must run directly.
- Include comments.
- Include error handling.
- Follow best practices.
"""
response = llm.invoke(prompt)

create_folder(project_name)

create_file(
    f"{project_name}/main.py",
    response.content
)

create_file(
    f"{project_name}/README.md",
    f"# {project_name}"
)

print(f"\nProject '{project_name}' created.")
