from selenium_agent import (
    google_search,
    get_title
)

print(
    google_search(
        "LangChain tutorial"
    )
)

input("Press Enter after page loads...")

print(
    get_title()
)
