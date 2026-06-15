from registry import TOOLS

while True:

    user = input("You: ").lower()

    if user == "exit":
        break

    if user in TOOLS:
        result = TOOLS[user]()
        print("Jarvis:", result)

    else:
        print("Jarvis: I don't know that command.")
