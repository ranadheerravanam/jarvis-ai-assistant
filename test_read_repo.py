from github_api import github_search
from selenium_agent import (
    open_repository,
    get_page_text
)

repo = github_search("langchain")

print(repo)

open_repository(repo["url"])

input("Wait until GitHub finishes loading, then press Enter...")

text = get_page_text()

print("\n========== PAGE ==========\n")

print(text[:5000])
