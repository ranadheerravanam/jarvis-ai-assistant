from langchain_ollama import ChatOllama
from tools import find_file, read_file
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("File to review: ")
llm = ChatOllama(model="llama3.2")

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("File to review: ")
paths = find_file.invoke(
    {"filename": filename}
)

path = paths.split("\n")[0]
print("\nPATH:")
print(path)
print()

if path == "File not found":
    print("File not found")
    exit()

content = read_file.invoke(
    {"filepath": path}
)
print(content[:500])
print("\n-----\n")

response = llm.invoke(
    f"""
You are a Senior Software Engineer.

Review this code.

Find:

1. Bugs
2. Logic Errors
3. Bad Practices
4. Security Risks
5. Performance Issues
6. Improvements

File:
{filename}

Code:

{content}
"""
)

print("\nBUG REPORT:\n")
print(response.content)
