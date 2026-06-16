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

print("=== Router Jarvis Started ===")
print("Type 'exit' to quit.\n")

while True:

    try:

        user = input("You: ")

        if user.lower() == "exit":
            print("Jarvis shutting down...")
            break

        # MEMORY SAVE
        if user.lower().startswith("remember"):

            fact = user[8:].strip()

            save_memory(fact)

            print("Jarvis: Memory saved.\n")

            continue

        # SHOW MEMORY
        if user.lower() == "show memory":

            memories = get_memories()

            print("\nStored Memories:")

            for memory in memories:
                print("-", memory)

            print()

            continue

        # WEB SEARCH
        if user.lower().startswith("search "):

            query = user[7:].strip()

            results = web_search.invoke(
                {"query": query}
            )

            answer = llm.invoke(
                f"""
Answer the question using these search results.

Question:
{query}

Results:
{results}
"""
            )

            print("\nJarvis:")
            print(answer.content)
            print()

            continue

        # READ FULL PATH
        if user.lower().startswith("read /"):

            filepath = user[5:].strip()

            result = read_file.invoke(
                {"filepath": filepath}
            )

            print("\nJarvis:")
            print(result)
            print()

            continue

        # EXPLAIN FILE
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

        # ANALYZE PROJECT
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
6. Suggested Improvements

Code:

{all_code[:15000]}
"""
            )

            print("\nJarvis:")
            print(analysis.content)
            print()

            continue

        # TOOL ROUTE
        if any(
            word in user.lower()
            for word in ["open", "launch", "start", "find"]
        ):

            response = llm_with_tools.invoke(user)

            if response.tool_calls:

                tool_call = response.tool_calls[0]

                tool_name = tool_call["name"]

                tool_args = tool_call.get("args", {})

                print(f"\nSelected Tool: {tool_name}")

                if tool_args:
                    print(f"Arguments: {tool_args}")

                result = tools[tool_name].invoke(tool_args)

                print(f"Jarvis: {result}")

            else:

                print(f"\nJarvis: {response.content}")

            print()

            continue

        # CHAT + MEMORY

        memories = get_memories()

        memory_text = "\n".join(memories)

        prompt = f"""
Known facts:

{memory_text}

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
