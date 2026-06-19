from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

def generate_file(project_type, filepath):

    prompt = f"""
You are a senior software engineer.

Project:
{project_type}

Generate code for:

{filepath}

Return ONLY code.

No markdown.
No explanations.
"""

    response = llm.invoke(prompt)

    code = response.content

    code = code.replace(
        "```python",
        ""
    )

    code = code.replace(
        "```",
        ""
    )

    return code.strip()
