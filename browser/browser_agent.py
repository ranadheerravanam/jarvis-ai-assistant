from browser_tools import (
    google_search,
    github_search,
    youtube_search,
    ott_search
)


def browser_agent(command):

    cmd = command.lower()
    if cmd.startswith("open netflix for"):

        query = command.replace(
            "open netflix for",
            ""
        ).strip()

        return ott_search(
           "netflix",
            query
        )

    elif cmd.startswith("open prime for"):

        query = command.replace(
            "open prime for",
            ""
        ).strip()

        return ott_search(
            "prime",
            query
        )

    elif cmd.startswith("open hotstar for"):

        query = command.replace(
            "open hotstar for",
            ""
        ).strip()

        return ott_search(
            "hotstar",
            query
        )

    elif cmd.startswith("google "):

        query = command[7:].strip()

        return google_search(query)

    elif cmd.startswith("github "):

        query = command[7:].strip()

        return github_search(query)

    elif cmd.startswith("youtube "):

        query = command[8:].strip()

        return youtube_search(query)

    elif cmd.startswith("netflix "):

        query = command[8:].strip()

        return ott_search(
            "netflix",
            query
        )

    elif cmd.startswith("prime "):

        query = command[6:].strip()

        return ott_search(
            "prime",
            query
        )

    elif cmd.startswith("hotstar "):

        query = command[8:].strip()

        return ott_search(
            "hotstar",
            query
        )

    return "Unknown browser command."
