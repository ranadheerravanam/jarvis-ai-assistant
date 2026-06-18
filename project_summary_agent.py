from tools import find_python_files

files = find_python_files.invoke({}).split("\n")

print("\nPROJECT SUMMARY\n")

print("Total Python Files:", len(files))

modules = []

for f in files:

    if "/rag/" in f:
        modules.append("PDF RAG")

    elif "/code_rag/" in f:
        modules.append("Code RAG")

    elif "memory" in f:
        modules.append("Memory")

    elif "agent" in f:
        modules.append("Agents")

unique_modules = sorted(set(modules))

print("\nDetected Modules:\n")

for m in unique_modules:
    print("-", m)
print("\nMain Entry:\n")

if any("jarvis_v3.py" in f for f in files):
    print("jarvis_v3.py")
print("\nTechnologies:\n")

print("- Ollama")
print("- ChromaDB")
print("- SQLite")
print("- LangChain")
print("\nPROJECT REPORT\n")

print("""
Strengths:
- PDF Question Answering
- Code Understanding
- Memory System
- Multi-Agent Architecture
- Autonomous Planning

Weaknesses:
- Browser Automation Incomplete
- No Architecture Graph
- No Automatic Code Modification
""")
