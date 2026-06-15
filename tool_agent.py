from langchain_ollama import ChatOllama
from tools import open_chrome, open_vscode

llm = ChatOllama(model="llama3.2")

tools = {
    "open_chrome": open_chrome,
    "open_vscode": open_vscode
}

llm_with_tools = llm.bind_tools(
    [open_chrome, open_vscode]
)

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    response = llm_with_tools.invoke(user)

    # Structured tool call
    if response.tool_calls:

        tool_name = response.tool_calls[0]["name"]

        result = tools[tool_name].invoke({})

        print("\nJarvis:", result)

    # Fallback for models returning JSON text
    elif "open_chrome" in response.content:

        result = open_chrome.invoke({})
        print("\nJarvis:", result)

    elif "open_vscode" in response.content:

        result = open_vscode.invoke({})
        print("\nJarvis:", result)

    else:

        print("\nJarvis:", response.content)

    print()
