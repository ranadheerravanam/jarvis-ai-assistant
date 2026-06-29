from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir="whatsapp_profile",
        headless=False,
    )

    page = context.new_page()

    page.goto("https://web.whatsapp.com")

    input("Open your own chat and press Enter...")

    while True:

        try:

            messages = page.locator(
                "div.copyable-text span.selectable-text"
            )

            count = messages.count()

            if count > 0:

                latest = messages.nth(count - 1).inner_text()

                print("\nLatest Message:")
                print(latest)

        except Exception as e:

            print(e)

        time.sleep(2)
