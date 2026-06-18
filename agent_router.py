from langchain_ollama import ChatOllama


import sys

if not sys.stdin.isatty():

    query = sys.stdin.read().strip()

else:

    query = input("Task: ")
llm = ChatOllama(model="llama3.2")
prompt = f"""
You are an agent router.

Available agents:

project_agent
file_agent
bug_finder
refactor_agent

Rules:

- If task contains "analyze my project" -> project_agent
- If task contains "explain" or "analyze" and a filename -> file_agent
- If task contains "bug", "issue", "problem", "review" -> bug_finder
- If task contains "refactor", "improve code", "optimize" -> refactor_agent

Return ONLY ONE WORD.

Task:
{query}
"""
q = query.lower()

if "review" in q or "bug" in q or "issue" in q:

    response_text = "bug_finder"

elif "refactor" in q or "optimize" in q or "improve" in q:

    response_text = "refactor_agent"

elif "explain" in q or "understand" in q:

    response_text = "file_agent"

elif "analyze my project" in q:

    response_text = "project_agent"
else:

    response = llm.invoke(prompt)

    response_text = response.content.strip()
print("\nAgent:")
print(response_text)

import subprocess

agent = response_text.lower()
filename = None

for word in query.split():

    if word.endswith(".py"):
        filename = word
        break

if agent == "bug_finder":

    subprocess.run(
        ["python", "bug_finder.py", filename or "tools.py"]
    )

elif agent == "refactor_agent":

    subprocess.run(
        ["python", "refactor_agent.py", filename or "tools.py"]
    )

elif agent == "file_agent":

    subprocess.run(
        ["python", "file_agent.py", filename or "tools.py"]
    )

elif agent == "project_agent":

    subprocess.run(
        ["python", "project_agent.py"]
    )

else:

    print("No suitable agent found.")
