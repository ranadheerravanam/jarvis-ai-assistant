from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    response = llm.invoke(user)

    print("\nJarvis:", response.content)
    print()
