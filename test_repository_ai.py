from github_api import github_search
from selenium_agent import (
    open_repository,
    get_page_text
)
from repository_ai import summarize_repository

repo = github_search("langchain")

print(repo)

open_repository(repo["url"])

input("Wait until GitHub loads then press Enter...")

page = get_page_text()

print("\nThinking...\n")

answer = summarize_repository(page)

print(answer)
