from langchain_ollama import ChatOllama
from browser_tools import ott_search
from tools import (
    open_chrome,
    open_vscode,
    open_terminal,
    open_files,
    open_calculator,
    find_python_files,
    find_file,
    read_file,
    web_search,
    open_youtube,
    open_netflix,
    open_prime,
    open_hotstar,
    open_vtop,
    open_youtube_personal,
    open_gmail_personal,
    open_netflix_personal,
    open_prime_personal,
    open_hotstar_personal,
)
from browser_tools import (
    youtube_search,
    google_search,
    github_search,
    ott_search
)
from memory import save_memory, get_memories

llm = ChatOllama(model="llama3.2")

tools = {
    "open_chrome": open_chrome,
    "open_vscode": open_vscode,
    "open_terminal": open_terminal,
    "open_files": open_files,
    "open_calculator": open_calculator,
    "find_python_files": find_python_files,
    "find_file": find_file,
    "read_file": read_file,
    "web_search": web_search,
    "open_youtube": open_youtube,
    "open_netflix": open_netflix,
    "open_prime": open_prime,
    "open_hotstar": open_hotstar,
    "open_vtop": open_vtop,
    "open_youtube_personal": open_youtube_personal,
    "open_gmail_personal": open_gmail_personal,
    "open_netflix_personal": open_netflix_personal,
    "open_prime_personal": open_prime_personal,
    "open_hotstar_personal": open_hotstar_personal,
}

llm_with_tools = llm.bind_tools(list(tools.values()))

print("=== Jarvis v2 Started ===")
print("Type 'exit' to quit.\n")

while True:

    try:

        user = input("You: ").strip()

        if user.lower() == "exit":
            print("Jarvis shutting down...")
            break

        # Identity route
        if user.lower() in ["hi", "hello", "hey"]:
            print("\nJarvis: Hello! I am Jarvis, your AI assistant.\n")
            continue

        if user.lower() in ["what is your name", "who are you"]:
            print("\nJarvis: I am Jarvis, your AI assistant.\n")
            continue

        # Memory save
        if user.lower().startswith("remember"):

            fact = user[8:].strip()

            save_memory(fact)

            print("\nJarvis: Memory saved.\n")

            continue

        # Show memory
        if user.lower() == "show memory":

            memories = get_memories()

            print("\nStored Memories:")

            for memory in memories:
                print("-", memory)

            print()

            continue
        # YouTube Search

        if user.lower().startswith("search youtube for"):

            query = user[18:].strip()

            print(
                "\nJarvis:",
                youtube_search(query)
            )
            print()

            continue


        # Google Search

        if user.lower().startswith("search google for"):

            query = user[17:].strip()

            print(
                "\nJarvis:",
                google_search(query)
            )
            print()

            continue


        # GitHub Search

        if user.lower().startswith("search github for"):

            query = user[17:].strip()

            print(
                "\nJarvis:",
                github_search(query)
            )
            print()

            continue
        # OTT SEARCH

        if user.lower().startswith("search netflix for"):

            query = user[len("search netflix for"):].strip()

            print("\nJarvis:", ott_search("netflix", query))
            print()

            continue

        if user.lower().startswith("search prime for"):

            query = user[len("search prime for"):].strip()

            print("\nJarvis:", ott_search("prime", query))
            print()

            continue

        if user.lower().startswith("search hotstar for"):

            query = user[len("search hotstar for"):].strip()

            print("\nJarvis:", ott_search("hotstar", query))
            print()

            continue

        if user.lower().startswith("search zee5 for"):

            query = user[len("search zee5 for"):].strip()

            print("\nJarvis:", ott_search("zee5", query))
            print()

            continue

        if user.lower().startswith("search sony for"):

            query = user[len("search sony for"):].strip()

            print("\nJarvis:", ott_search("sony", query))
            print()

            continue
        # Web search
        if user.lower().startswith("search "):

            query = user[7:].strip()

            results = web_search.invoke(
                {"query": query}
            )

            answer = llm.invoke(
                f"""
Answer using these search results.

Question:
{query}

Results:
{results}
"""
            )

            print("\nJarvis:", answer.content)
            print()

            continue

        # Read file by full path
        if user.lower().startswith("read /"):

            filepath = user[5:].strip()

            result = read_file.invoke(
                {"filepath": filepath}
            )

            print("\nJarvis:")
            print(result)
            print()

            continue

        # Explain file
        if user.lower().startswith("explain "):

            filename = user[8:].strip()

            path = find_file.invoke(
                {"filename": filename}
            )

            if path == "File not found":

                print("\nJarvis: File not found.\n")

                continue

            content = read_file.invoke(
                {"filepath": path}
            )

            explanation = llm.invoke(
                f"""
Explain this Python file.

Filename:
{filename}

Code:
{content}
"""
            )

            print("\nJarvis:")
            print(explanation.content)
            print()

            continue

        # Analyze project
        if user.lower() == "analyze my project":

            files = find_python_files.invoke({})

            all_code = ""

            for file in files.split("\n"):

                try:

                    content = read_file.invoke(
                        {"filepath": file}
                    )

                    all_code += f"\n\nFILE: {file}\n"
                    all_code += content

                except Exception:
                    pass

            analysis = llm.invoke(
                f"""
Analyze this software project.

Explain:
1. Purpose
2. Architecture
3. Main Components
4. Strengths
5. Weaknesses
6. Improvements

Code:

{all_code[:15000]}
"""
            )

            print("\nJarvis:")
            print(analysis.content)
            print()

            continue
# PERSONAL ACCOUNT ROUTES

        if "youtube" in user.lower() and "personal" in user.lower():

            print(
                "\nJarvis:",
                open_youtube_personal.invoke({})
            )
            print()

            continue


        if "gmail" in user.lower() and "personal" in user.lower():

            print(
                "\nJarvis:",
                open_gmail_personal.invoke({})
            )
            print()

            continue


        if "netflix" in user.lower() and "personal" in user.lower():

            print(
                "\nJarvis:",
                open_netflix_personal.invoke({})
            )
            print()

            continue


        if "prime" in user.lower() and "personal" in user.lower():

            print(
                "\nJarvis:",
                open_prime_personal.invoke({})
            )
            print()

            continue


        if "hotstar" in user.lower() and "personal" in user.lower():

            print(
                "\nJarvis:",
                open_hotstar_personal.invoke({})
            )
            print()

            continue
# MULTI COMMAND ROUTE

        if " and " in user.lower():

            cmd = user.lower()

            if "youtube" in cmd:
                print(open_youtube_personal.invoke({}))

            if "gmail" in cmd:
                print(open_gmail_personal.invoke({}))

            if "netflix" in cmd:
                print(open_netflix_personal.invoke({}))

            if "prime" in cmd:
                print(open_prime_personal.invoke({}))

            if "hotstar" in cmd:
                print(open_hotstar_personal.invoke({}))

            if "chrome" in cmd:
                print(open_chrome.invoke({}))

            if "vscode" in cmd:
                print(open_vscode.invoke({}))

            if "terminal" in cmd:
                print(open_terminal.invoke({}))

            print()

            continue
        # Tool route
        if any(
            word in user.lower()
            for word in ["open", "launch", "start", "find"]
        ):

            response = llm_with_tools.invoke(user)

            if response.tool_calls:

                tool_call = response.tool_calls[0]

                tool_name = tool_call["name"]

                tool_args = tool_call.get("args", {})

                result = tools[tool_name].invoke(tool_args)

                print(f"\nJarvis: {result}")
                print()

            else:

                print(f"\nJarvis: {response.content}")
                print()

            continue

        # Chat + memory

        memories = get_memories()

        prompt = f"""
You are Jarvis, a helpful AI assistant.

Known facts:
{chr(10).join(memories)}

Rules:
- Use memory only when relevant.
- Don't mention memory unless needed.
- If asked your name, say you are Jarvis.

User:
{user}
"""

        response = llm.invoke(prompt)

        print("\nJarvis:", response.content)
        print()

    except KeyboardInterrupt:

        print("\nJarvis shutting down...")
        break

    except Exception as e:

        print("\nError:", e)
