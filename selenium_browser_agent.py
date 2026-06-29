from selenium_agent import (
    open_site,
    google_search,
    github_search,
    youtube_search
)

def browser_agent(command):

    command = command.lower().strip()

    if command == "open github":
        return open_site("https://github.com")

    elif command == "open google":
        return open_site("https://google.com")

    elif command == "open youtube":
        return open_site("https://youtube.com")

    elif command.startswith("google "):
        query = command.replace("google ", "")
        return google_search(query)

    elif command.startswith("github "):
        query = command.replace("github ", "")
        return github_search(query)

    elif command.startswith("youtube "):
        query = command.replace("youtube ", "")
        return youtube_search(query)

    return "Unknown browser command."
