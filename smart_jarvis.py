from langchain_ollama import ChatOllama

from tools import (
    open_chrome,
    open_vscode,
    open_terminal,
    open_files,
    open_calculator,
    find_python_files,
    find_file,
    read_file
)

from memory import save_memory, get_memories


# LLM
llm = ChatOllama(
    model="llama3.2"
)

# Tool Registry
tools = {
    "open_chrome": open_chrome,
    "open_vscode": open_vscode,
    "open_terminal": open_terminal,
    "open_files": open_files,
    "open_calculator": open_calculator,
    "find_python_files": find_python_files,
    "find_file": find_file,
    "read_file": read_file
}

# Bind tools
llm_with_tools = llm.bind_tools(
    list(tools.values())
)

SYSTEM_PROMPT = """
You are Jarvis.

Available tools:

- open_chrome
- open_vscode
- open_terminal
- open_files
- open_calculator
- find_python_files
- find_file
- read_file

Rules:

1. Use tools whenever appropriate.
2. If the user asks to find a file, use find_file.
3. If the user asks to read a file, use read_file.
4. If the user asks to open software, use the matching tool.
5. Use memories to answer personal questions.
"""

print("=== Smart Jarvis Started ===")
print("Type 'exit' to quit.\n")

while True:

    try:

        user = input("You: ")

        if user.lower() == "exit":
            print("Jarvis shutting down...")
            break

        # Save memory
        if user.lower().startswith("remember"):

            fact = user[8:].strip()

            save_memory(fact)

            print("Jarvis: Memory saved.\n")

            continue

        # Show memory
        if user.lower() == "show memory":

            memories = get_memories()

            print("\nStored Memories:")

            for m in memories:
                print("-", m)

            print()

            continue

        # Load memories
        memories = get_memories()

        memory_text = "\n".join(memories)

        prompt = f"""
{SYSTEM_PROMPT}

Known facts:

{memory_text}

User request:
{user}
"""

        response = llm.invoke(prompt)

        # Tool Calls
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

    except KeyboardInterrupt:

        print("\n\nJarvis shutting down...")
        break

    except Exception as e:

        print(f"\nError: {e}")
