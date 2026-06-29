from selenium_agent import open_site, get_title, get_current_url

print(open_site("https://github.com"))

input("Wait for page to load and press Enter...")

print("TITLE:", get_title())
print("URL:", get_current_url())
