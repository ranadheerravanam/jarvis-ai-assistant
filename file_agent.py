from langchain_ollama import ChatOllama
from tools import find_file, read_file
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("File name: ")

llm = ChatOllama(model="llama3.2")

paths = find_file.invoke(
    {"filename": filename}
)

path = paths.split("\n")[0]
print("\nPATH FOUND:")
print(path)
print()

if path == "File not found":
    print("File not found")
    exit()

content = read_file.invoke(
    {"filepath": path}
)

response = llm.invoke(
    f"""
Explain this Python file.

File:
{filename}

Code:
{content}
"""
)

print("\nAnalysis:\n")
print(response.content)
