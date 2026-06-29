from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote

driver = None


def get_driver():
    global driver

    if driver is None:

        options = Options()

        # Uncomment these only after everything works
        # options.add_argument(
        #     "--user-data-dir=/home/ranadheer/.config/google-chrome"
        # )
        #
        # options.add_argument(
        #     "--profile-directory=Profile 3"
        # )

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


def google_search(query):
    d = get_driver()
    d.get(
        f"https://www.google.com/search?q={quote(query)}"
    )
    return f"Searched Google for {query}"


def youtube_search(query):
    d = get_driver()
    d.get(
        f"https://www.youtube.com/results?search_query={quote(query)}"
    )
    return f"Searched YouTube for {query}"


def github_search(query):
    d = get_driver()
    d.get(
        f"https://github.com/search?q={quote(query)}"
    )
    return f"Searched GitHub for {query}"


def google_search_box(query):
    d = get_driver()

    d.get("https://www.google.com")

    search_box = WebDriverWait(d, 10).until(
        EC.presence_of_element_located(
            (By.NAME, "q")
        )
    )

    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)

    return f"Searched Google for {query}"
def github_open_first_result(query):

    d = get_driver()

    d.get(
        f"https://github.com/search?q={quote(query)}&type=repositories"
    )

    wait = WebDriverWait(d, 20)

    repo = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//a[contains(@href,'/') and contains(text(),'/')]"
            )
        )
    )

    href = repo.get_attribute("href")

    print("Opening:", href)

    d.get(href)

    return "Repository opened"
def get_title():
    d = get_driver()
    return d.title


def get_current_url():
    d = get_driver()
    return d.current_url


def get_page_text():
    d = get_driver()
    return d.find_element(By.TAG_NAME, "body").text[:3000]


def close_browser():
    global driver

    if driver:

        driver.quit()
        driver = None

    return "Browser closed"
def get_page_title():
    d = get_driver()
    return d.title


def get_page_text():
    d = get_driver()
    return d.find_element(By.TAG_NAME, "body").text


def get_links():
    d = get_driver()

    links = d.find_elements(By.TAG_NAME, "a")

    return [
        l.get_attribute("href")
        for l in links
        if l.get_attribute("href")
    ]
from selenium.webdriver.common.by import By


def get_page_text():

    d = get_driver()

    body = d.find_element(
        By.TAG_NAME,
        "body"
    )

    return body.text
def open_repository(url):

    d = get_driver()

    d.get(url)

    return f"Opened {url}"
def get_page_text():

    d = get_driver()

    wait = WebDriverWait(d, 20)

    body = wait.until(
        EC.presence_of_element_located(
            (By.TAG_NAME, "body")
        )
    )

    return body.text
