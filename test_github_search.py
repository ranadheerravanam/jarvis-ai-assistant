from selenium_agent import get_driver
from urllib.parse import quote

driver = get_driver()

driver.get(
    f"https://github.com/search?q={quote('langchain')}&type=repositories"
)

input("Press Enter after the page loads...")

print("TITLE:", driver.title)
print("URL:", driver.current_url)
