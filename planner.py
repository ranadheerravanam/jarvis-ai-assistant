from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")


def make_plan(task):

    prompt = f"""
You are Jarvis Planner.

Available Tools:

1. find_python_files
2. read_file
3. web_search
4. find_file

Create a step-by-step plan using ONLY these tools.

Task:
{task}

Return numbered steps.
"""

    response = llm.invoke(prompt)

    return response.content
