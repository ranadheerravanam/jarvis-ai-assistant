from rag_engine import ask_rag
while True:

    q = input("Question: ")

    if q == "exit":
        break

    print()
    print(ask_rag(q))
    print()
