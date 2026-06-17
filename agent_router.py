from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

query = input("Task: ")

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

response = llm.invoke(prompt)

print("\nAgent:")
print(response.content.strip())
import subprocess

agent = response.content.strip().lower()

print("\nAgent:", agent)

if agent == "bug_finder":
    subprocess.run([
        "python",
        "bug_finder.py",
        "tools.py"
    ])
elif agent == "project_agent":
    subprocess.run(["python", "project_agent.py"])

elif agent == "file_agent":
    subprocess.run(["python", "file_agent.py"])

elif agent == "refactor_agent":
    subprocess.run(["python", "refactor_agent.py"])

else:
    print("No suitable agent found.")
