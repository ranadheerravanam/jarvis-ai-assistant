import sys
from pathlib import Path

# Add the project root (~/jarvis) to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT)
from playwright.sync_api import sync_playwright
from core.processor import process
import time

last_message = ""

with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir="whatsapp_profile",
        headless=False,
    )

    page = context.new_page()

    page.goto("https://web.whatsapp.com")

    input("Open your own WhatsApp chat and press Enter...")

    while True:

        try:

            messages = page.locator(
                "div.copyable-text span.selectable-text"
            )

            count = messages.count()

            if count == 0:
                time.sleep(1)
                continue

            latest = messages.nth(count - 1).inner_text()

            if latest != last_message:

                print("\nNew Message:", latest)

                last_message = latest

                reply = process(latest)

                print("Reply:", reply)

                box = page.locator(
                    'div[contenteditable="true"]'
                ).last

                box.click()

                box.fill(reply)

                page.keyboard.press("Enter")

        except Exception as e:

            print(e)

        time.sleep(2)
