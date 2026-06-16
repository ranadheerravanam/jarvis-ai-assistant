from memory import save_memory, get_memories

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    if user.lower().startswith("remember"):

        fact = user.replace("remember", "").strip()

        print(save_memory(fact))

    elif "memory" in user.lower():

        memories = get_memories()

        print("\nStored Memories:")

        for m in memories:
            print("-", m)

    else:

        print("I don't understand.")
