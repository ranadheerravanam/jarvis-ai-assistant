from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.binary_location = "/snap/bin/chromium"

options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get("https://google.com")

input("Press Enter...")

driver.quit()
