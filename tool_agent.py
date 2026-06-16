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
    "read_file":read_file
}

# Bind tools
llm_with_tools = llm.bind_tools(
    list(tools.values())
)

print("=== Jarvis Started ===")
print("Type 'exit' to quit.\n")

SYSTEM_PROMPT = """
You are Jarvis.

Rules:

1. If the user wants Chrome, browser, internet browsing:
   use open_chrome.

2. If the user wants VS Code, coding editor:
   use open_vscode.

3. If the user wants a terminal, shell, console:
   use open_terminal.

4. If the user wants calculator:
   use open_calculator.

5. If the user wants file explorer or file manager:
   use open_files.

6. If the user wants to find all python files:
   use find_python_files.

7. If the user wants to locate a specific file:
   use find_file.

Examples:

User: Find tool_agent.py
Tool: find_file

User: Locate settings.py
Tool: find_file

User: Search for README.md
Tool: find_file

Always prefer tools when available.
"""

while True:

    try:

        user = input("You: ")

        if user.lower() == "exit":
            print("Jarvis shutting down...")
            break

        prompt = f"""
{SYSTEM_PROMPT}

User request:
{user}
"""

        response = llm_with_tools.invoke(prompt)

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

            print("\nJarvis:", response.content)

        print()

    except KeyboardInterrupt:

        print("\n\nJarvis shutting down...")
        break

    except Exception as e:

        print(f"\nError: {e}")
