from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = None

def get_driver():

    global driver

    if driver is None:

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            )
        )

    return driver


def open_site(url):

    d = get_driver()

    d.get(url)

    return f"Opened {url}"
