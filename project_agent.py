from langchain_ollama import ChatOllama

from tools import (
    find_python_files,
    read_file
)

llm = ChatOllama(model="llama3.2")

print("Analyzing project...\n")

files = find_python_files.invoke({})

all_code = ""

for file in files.split("\n"):

    try:

        content = read_file.invoke(
            {"filepath": file}
        )

        all_code += f"\n\nFILE: {file}\n"
        all_code += content

    except Exception:
        pass

analysis = llm.invoke(
    f"""
Analyze this software project.

Explain:

1. Purpose
2. Architecture
3. Components
4. Strengths
5. Weaknesses
6. Improvements

Code:

{all_code[:15000]}
"""
)

print(analysis.content)
