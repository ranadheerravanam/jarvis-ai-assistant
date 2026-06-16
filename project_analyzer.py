from langchain_ollama import ChatOllama
from tools import find_python_files, read_file

llm = ChatOllama(
    model="llama3.2"
)

files = find_python_files.invoke({})

print("Files Found:\n")
print(files)

all_code = ""

for file in files.split("\n")[:10]:

    try:

        code = read_file.invoke(
            {"filepath": file}
        )

        all_code += f"\n\nFILE: {file}\n"
        all_code += code

    except:

        pass

analysis = llm.invoke(
    f"""
Analyze this Python project.

Explain:

1. What the project does
2. Architecture
3. Strengths
4. Weaknesses
5. Improvements

Code:

{all_code}
"""
)

print("\nProject Analysis:\n")
print(analysis.content)
