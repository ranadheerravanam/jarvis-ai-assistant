from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2"
)

def fix_code(code, error):

    prompt = f"""
You are an expert Python developer.

Fix the code.

Return ONLY corrected code.

CODE:

{code}

ERROR:

{error}
"""

    response = llm.invoke(prompt)

    return response.content
