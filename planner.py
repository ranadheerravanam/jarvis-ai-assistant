from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")


def make_plan(task):

    prompt = f"""
You are Jarvis Planner.

Available tools:

find_python_files
read_file
find_file
web_search

Create a plan.

Rules:
- Return ONLY tool names.
- One tool per line.
- No explanations.
- No bullet points.
- No numbering.

Task:
{task}
"""

    response = llm.invoke(prompt)

    return response.content
