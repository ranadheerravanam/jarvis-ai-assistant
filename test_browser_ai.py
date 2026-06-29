from browser_ai_agent import browser_ai

while True:

    command = input("Command: ")

    if command.lower() == "exit":
        break

    print()

    result = browser_ai(command)

    print("\n========== AI RESPONSE ==========\n")

    print(result)

    print("\n===============================\n")
