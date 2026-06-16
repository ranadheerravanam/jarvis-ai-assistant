from langchain_ollama import ChatOllama
from memory import save_memory, get_memories

llm = ChatOllama(
    model="llama3.2"
)

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    # Save memory
    if user.lower().startswith("remember"):

        fact = user[8:].strip()

        save_memory(fact)

        print("Jarvis: Memory saved.")

        continue

    # Load memories
    memories = get_memories()

    prompt = f"""
You are Jarvis.

Known facts:

{chr(10).join(memories)}

User:
{user}
"""

    response = llm.invoke(prompt)

    print("\nJarvis:", response.content)
    print()
