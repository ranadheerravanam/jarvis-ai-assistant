from github_api import github_search
from selenium_agent import open_repository

repo = github_search("langchain")

print(repo)

open_repository(repo["url"])

input("Press Enter to exit...")
