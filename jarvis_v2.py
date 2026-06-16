from langchain_ollama import ChatOllama
from tools import (
    open_chrome,
    open_vscode,
    open_terminal,
    open_files,
    open_calculator,
    find_python_files,
    find_file,
    read_file,
    web_search
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
    "web_search": web_search
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
