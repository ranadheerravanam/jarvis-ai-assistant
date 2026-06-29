import sys
import time
from pathlib import Path

# Add ~/jarvis to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from playwright.sync_api import sync_playwright
from core.processor import process


last_message = ""


with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir="whatsapp_profile",
        headless=False,
    )

    page = context.new_page()

    page.goto("https://web.whatsapp.com")

    input("Open your own WhatsApp chat and press Enter...")

    print("Jarvis WhatsApp Controller Started...\n")

    while True:

        try:

            messages = page.locator(
                "div.copyable-text span.selectable-text"
            )

            count = messages.count()

            if count == 0:
                time.sleep(1)
                continue

            latest = messages.nth(count - 1).inner_text().strip()

            if latest != last_message:

                last_message = latest

                print("\n========================")
                print("Received :", latest)

                try:
                    reply = process(latest)
                except Exception as e:
                    reply = f"Error: {e}"

                print("Reply :", reply)

                box = page.locator(
                    'div[contenteditable="true"]'
                ).last

                box.click()

                box.fill(str(reply))

                page.keyboard.press("Enter")

            time.sleep(2)

        except KeyboardInterrupt:

            print("\nStopping controller...")

            break

        except Exception as e:

            print("Controller Error:", e)

            time.sleep(2)

    context.close()
