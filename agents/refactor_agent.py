from langchain_ollama import ChatOllama
from tools import find_file, read_file
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("File to refactor: ")
llm = ChatOllama(model="llama3.2")


path = find_file.invoke(
    {"filename": filename}
)

if path == "File not found":
    print("File not found")
    exit()

content = read_file.invoke(
    {"filepath": path}
)

response = llm.invoke(
    f"""
You are a Senior Python Engineer.

Refactor this code.

Requirements:

1. Improve readability
2. Improve performance
3. Remove duplicate code
4. Improve error handling
5. Follow Python best practices

Return:

- Problems found
- Refactored code
- Explanation

Code:

{content}
"""
)

print(response.content)
