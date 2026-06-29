from core.processor import process

print("=" * 50)
print("        JARVIS v4")
print("=" * 50)

while True:

    command = input("\nYou: ")

    if command.lower() == "exit":
        break

    try:

        reply = process(command)

        print("\nJarvis:")
        print(reply)

    except Exception as e:

        print("\nError:")
        print(e)
