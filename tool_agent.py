from langchain_ollama import ChatOllama
from tools import (
    open_chrome,
    open_vscode,
    open_terminal,
    open_files,
    open_calculator,
    find_python_files
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
    "find_python_files": find_python_files
}
# Bind tools to the LLM
llm_with_tools = llm.bind_tools(
    list(tools.values())
)

print("=== Jarvis Started ===")
print("Type 'exit' to quit.\n")

while True:

    try:
        user = input("You: ")

        if user.lower() == "exit":
            print("Jarvis shutting down...")
            break

        response = llm_with_tools.invoke(user)

        # Structured Tool Calls
        if response.tool_calls:

            tool_name = response.tool_calls[0]["name"]

            print(f"\nSelected Tool: {tool_name}")

            result = tools[tool_name].invoke({})

            print(f"Jarvis: {result}")

        # Fallback for models that return tool names as text
        elif "open_chrome" in response.content:

            print("\nSelected Tool: open_chrome")
            print("Jarvis:", open_chrome.invoke({}))

        elif "open_vscode" in response.content:

            print("\nSelected Tool: open_vscode")
            print("Jarvis:", open_vscode.invoke({}))

        elif "open_terminal" in response.content:

            print("\nSelected Tool: open_terminal")
            print("Jarvis:", open_terminal.invoke({}))

        elif "open_files" in response.content:

            print("\nSelected Tool: open_files")
            print("Jarvis:", open_files.invoke({}))

        elif "open_calculator" in response.content:

            print("\nSelected Tool: open_calculator")
            print("Jarvis:", open_calculator.invoke({}))

        else:

            print("\nJarvis:", response.content)

        print()

    except KeyboardInterrupt:

        print("\n\nJarvis shutting down...")
        break

    except Exception as e:

        print(f"\nError: {e}")
