from langchain_ollama import ChatOllama
from rag.rag_engine import ask_rag
from code_rag.code_engine import ask_code
from memory import save_memory, get_memories
from tools import *

import subprocess

llm = ChatOllama(model="llama3.2")

print("=== Jarvis v3 ===")
print("Type exit to quit\n")

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    # MEMORY SAVE

    if user.lower().startswith("remember"):

        fact = user[8:].strip()

        save_memory(fact)

        print("\nJarvis:")
        print("Memory saved.")
        print()

        continue
    # SHOW MEMORY

    if user.lower() == "show memory":

        memories = get_memories()

        print("\nJarvis:")

        for m in memories:
            print("-", m)

        print()

        continue


    # PDF RAG

    if user.lower().startswith("ask pdf"):

        question = user[7:].strip()

        answer = ask_rag(question)

        print("\nJarvis:")
        print(answer)
        print()

        continue
    # PROJECT ANALYSIS

    if "analyze my project" in user.lower():

        subprocess.run(
            ["python", "project_agent.py"]
        )

        continue

    # BUG FINDER

    if user.lower().startswith("bug"):

        parts = user.split()

        if len(parts) > 1:

            filename = parts[-1]

            subprocess.run(
                ["python", "bug_finder.py", filename]
            )

        continue

    # REFACTOR

    if user.lower().startswith("refactor"):

        parts = user.split()

        if len(parts) > 1:

            filename = parts[-1]

            subprocess.run(
                ["python", "refactor_agent.py", filename]
            )

        continue

    # FILE EXPLANATION

    if user.lower().endswith(".py"):

        filename = user.split()[-1]

        subprocess.run(
            ["python", "file_agent.py", filename]
        )

        continue
    # OPEN CHROME

    if "open chrome" in user.lower():

        print("\nJarvis:")
        print(open_chrome.invoke({}))
        print()

        continue

    # OPEN VSCODE

    if "open vscode" in user.lower():

        print("\nJarvis:")
        print(open_vscode.invoke({}))
        print()

        continue

    # OPEN TERMINAL

    if "open terminal" in user.lower():

        print("\nJarvis:")
        print(open_terminal.invoke({}))
        print()

        continue

    # WEB SEARCH

    if user.lower().startswith("search"):

        query = user[6:].strip()

        result = web_search.invoke(
            {"query": query}
        )

        print("\nJarvis:")
        print(result)
        print()

        continue

    # OPEN YOUTUBE

    if "open youtube" in user.lower():

        print("\nJarvis:")
        print(open_youtube.invoke({}))
        print()

        continue

    # NORMAL CHAT
    # CODE RAG

    if user.lower().startswith("ask code"):

        question = user[8:].strip()

        answer = ask_code(question)

        print("\nJarvis:")
        print(answer)
        print()

        continue
    memories = get_memories()

    prompt = f"""
You are Jarvis.

Known facts:

{chr(10).join(memories)}

User:
{user}
"""

    response = llm.invoke(prompt)
    print("\nJarvis:")
    print(response.content)
    print()
    if user.lower().startswith("search"):

        print("DEBUG: SEARCH ROUTE HIT")

        query = user[6:].strip()
