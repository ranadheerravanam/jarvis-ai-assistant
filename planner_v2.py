from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

def make_plan(task):

    prompt = f"""
You are an autonomous software engineering agent.

Task:
{task}

Generate 3-5 concrete actions needed to complete the task.

Rules:
- Do NOT explain planning.
- Do NOT explain objectives.
- Do NOT explain methodology.
- Return only actionable steps.
- Each step must directly help solve the task.

Example:

Task:
Review tools.py and suggest improvements

Output:

1. Read tools.py
2. Analyze functions and architecture
3. Identify bugs and code smells
4. Suggest refactoring opportunities
5. Generate improvement report
"""

    response = llm.invoke(prompt)

    return response.content
