from langchain_ollama import ChatOllama
from tools import *

llm = ChatOllama(model="llama3.2")

print("=== Jarvis v3 ===")
print("Type exit to quit\n")

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    # PROJECT ANALYSIS

    if "analyze my project" in user.lower():

        import subprocess

        subprocess.run(
            ["python", "project_agent.py"]
        )

        continue

    # BUG FINDER

    if "bug" in user.lower():

        import subprocess

        filename = user.split()[-1]

        subprocess.run(
            ["python", "bug_finder.py", filename]
        )

        continue
    # REFACTOR

    if "refactor" in user.lower():

        import subprocess
        filename=user.split()[-1]
        subprocess.run(
            ["python", "refactor_agent.py",filename]
        )

        continue

    # FILE EXPLANATION

    if ".py" in user.lower():

        import subprocess
        filename=user.split()[-1]
        subprocess.run(
            ["python", "file_agent.py",filename]
        )

        continue

    # NORMAL CHAT

    response = llm.invoke(user)

    print("\nJarvis:")
    print(response.content)
    print()
