from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir="whatsapp_profile",
        headless=False,
    )

    page = context.new_page()

    page.goto("https://web.whatsapp.com")

    input("Press Enter to close...")

    context.close()
