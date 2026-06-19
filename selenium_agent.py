from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = None

def get_driver():

    global driver

    if driver is None:

        options = Options()

        options.add_argument(
            "--user-data-dir=/home/ranadheer/.config/google-chrome"
        )

        options.add_argument(
            "--profile-directory=Profile 2"
        )

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=options
        )

    return driver


def open_site(url):

    d = get_driver()

    d.get(url)

    return f"Opened {url}"
