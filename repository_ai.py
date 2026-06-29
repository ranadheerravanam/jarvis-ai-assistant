from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")


def summarize_repository(page):

    prompt = f"""
You are an expert software engineer.

Read the GitHub repository page below and explain it.

Repository Page:

{page[:6000]}

Explain:

1. What is this repository?
2. What problem does it solve?
3. Main features
4. Technologies used
5. Who should use it?
6. Give a beginner-friendly explanation.
"""

    response = llm.invoke(prompt)

    return response.content
