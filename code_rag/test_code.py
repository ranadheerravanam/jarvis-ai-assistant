from code_engine import ask_code

while True:

    q = input("Question: ")

    if q.lower() == "exit":
        break

    print()
    print(ask_code(q))
    print()
