def normalize(command):

    cmd = command.lower().strip()

    # Remove "jarvis"
    if cmd.startswith("jarvis"):
        cmd = cmd[6:].strip()

    aliases = {

        "vscode": "open vscode",
        "code": "open vscode",

        "chrome": "open chrome",
        "browser": "open chrome",

        "terminal": "open terminal",

        "youtube": "open youtube",

        "google": "google",

        "github": "github",

        "netflix": "open netflix",

        "prime": "open prime",

        "hotstar": "open hotstar",
    }

    words = cmd.split()

    if len(words) == 1 and words[0] in aliases:
        return aliases[words[0]]

    return cmd
