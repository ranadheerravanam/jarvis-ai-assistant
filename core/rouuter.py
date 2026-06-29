def normalize(command):

    cmd = command.lower().strip()

    if cmd.startswith("jarvis"):
        cmd = cmd[6:].strip()

    aliases = {

        "vscode": "open vscode",
        "code": "open vscode",

        "chrome": "open chrome",
        "browser": "open chrome",

        "terminal": "open terminal",

        "calculator": "open calculator",

        "files": "open files",

        "youtube": "open youtube",

        "netflix": "open netflix",

        "prime": "open prime",

        "hotstar": "open hotstar",
    }

    words = cmd.split()

    if len(words) == 1:

        return aliases.get(words[0], cmd)

    return cmd
