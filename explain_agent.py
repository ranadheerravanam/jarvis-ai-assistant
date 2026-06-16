from langchain_ollama import ChatOllama

from tools import (
    find_file,
    read_file
)

llm = ChatOllama(
    model="llama3.2"
)

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    filename = user.replace("Explain", "").replace("explain", "").strip()

    path = find_file.invoke(
        {"filename": filename}
    )

    print("\nFound File:")
    print(path)

    content = read_file.invoke(
        {"filepath": path}
    )

    explanation = llm.invoke(
        f"""
Explain this Python code in simple terms.

Code:

{content}
"""
    )

    print("\nJarvis:")
    print(explanation.content)
    print()
