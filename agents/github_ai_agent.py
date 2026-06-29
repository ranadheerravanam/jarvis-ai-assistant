from github_api import github_search
from selenium_agent import (
    open_repository,
    get_page_text
)
from repository_ai import summarize_repository


def github_ai(query):

    query = query.lower().strip()

    if query.startswith("github "):
        query = query.replace("github ", "", 1)

    repo = github_search(query)
    if repo is None:
        return "Repository not found."

    print(f"\nFound: {repo['name']}")

    open_repository(repo["url"])

    input("\nWait until GitHub loads, then press Enter...")

    page = get_page_text()

    print("\nAnalyzing repository...\n")

    return summarize_repository(page)
