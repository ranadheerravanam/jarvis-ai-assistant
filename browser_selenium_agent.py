from selenium_agent import open_site


def browser_command(command):

    cmd = command.lower()

    if cmd == "open github":

        return open_site(
            "https://github.com"
        )

    if cmd == "open gmail":

        return open_site(
            "https://mail.google.com"
        )

    if cmd == "open youtube":

        return open_site(
            "https://youtube.com"
        )

    return "Unknown command"
