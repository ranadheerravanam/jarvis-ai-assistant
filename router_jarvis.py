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


llm = ChatOllama(model="llama3.2")

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

llm_with_tools = llm.bind_tools(list(tools.values()))

print("=== Router Jarvis Started ===")
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

            for memory in memories:
                print("-", memory)

            print()

            continue

        # Direct file read
        if user.lower().startswith("read /"):

            filepath = user[5:].strip()

            result = read_file.invoke(
                {"filepath": filepath}
            )

            print("\nJarvis:", result)
            print()

            continue

        # Tool route
        if any(
            word in user.lower()
            for word in ["open", "launch", "start", "find", "read"]
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

        # Chat + Memory route

        memories = get_memories()

        memory_text = "\n".join(memories)

        prompt = f"""
You are Jarvis.

Known facts:

{memory_text}

User:
{user}
"""

        response = llm.invoke(prompt)

        print(f"\nJarvis: {response.content}")
        print()

    except KeyboardInterrupt:

        print("\n\nJarvis shutting down...")
        break

    except Exception as e:

        print(f"\nError: {e}")
