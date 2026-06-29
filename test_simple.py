from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(
        ChromeDriverManager().install()
    )
)

print("Driver created")

driver.get("https://github.com")

print("GitHub opened")

input("Press Enter...")
