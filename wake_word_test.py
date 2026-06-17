from voice import listen, speak

WAKE_WORD = "jarvis"

while True:

    command = listen()

    if not command:
        continue

    if not command.startswith(WAKE_WORD):

        print("Ignored")
        continue

    command = command.replace(
        WAKE_WORD,
        "",
        1
    ).strip()

    speak(f"You said {command}")
