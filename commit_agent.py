from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2"
)


def generate_commit(changes):

    prompt = f"""
Generate a short git commit message.

Changes:

{changes}

Return only the commit message.
"""

    response = llm.invoke(prompt)

    return response.content.strip()
