from langchain_ollama import ChatOllama
from rag.rag_engine import ask_rag
from code_rag.code_engine import ask_code
from browser_agent import browser_agent
from memory import save_memory, get_memories
from tools import *
from browser_tools import (
    youtube_search,
    google_search,
    github_search,
    ott_search
)
import subprocess

llm = ChatOllama(model="llama3.2")

print("=== Jarvis v3 ===")
print("Type exit to quit\n")
while True:

    user = input("You: ")
    # PROJECT SUMMARY

    if user.lower() == "analyze my project":

        subprocess.run(
            ["python", "project_summary_agent.py"]
        )

        continue
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
    # AGENT ROUTER

    if ".py" in user.lower():

        import subprocess

        subprocess.run(
            ["python", "agent_router.py"],
            input=user,
            text=True
        )

        continue
    # YOUTUBE SEARCH

    if user.lower().startswith("youtube"):

        query = user[7:].strip()

        print("\nJarvis:")

        print(
            youtube_search(query)
        )

        print()

        continue
# GOOGLE SEARCH

    if user.lower().startswith("google"):

        query = user[6:].strip()

        print("\nJarvis:")

        print(
            google_search(query)
        )

        print()

        continue
# GITHUB SEARCH

    if user.lower().startswith("github"):

        query = user[6:].strip()

        print("\nJarvis:")

        print(
            github_search(query)
        )

        print()

        continue
# NETFLIX SEARCH

    if user.lower().startswith("netflix"):

        query = user[7:].strip()

        print("\nJarvis:")

        print(
            ott_search(
                "netflix",
                query
            )
        )


        print()

        continue
    if user.lower().startswith(
        (
            "google",
            "github",
            "youtube",
            "netflix",
            "prime",
            "hotstar",
            "open netflix",
            "open hotstar",
            "open prime"
        )
    ):

        print("\nJarvis:")

        print(
            browser_agent(user)
        )

        print()

        continue
    # NORMAL CHAT

    response = llm.invoke(user)

    print("\nJarvis:")
    print(response.content)
    print()
