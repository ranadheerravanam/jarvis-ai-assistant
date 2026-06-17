from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

def make_plan(task):

    prompt = f"""
Create a numbered plan.

Task:
{task}
"""

    response = llm.invoke(prompt)

    return response.content
