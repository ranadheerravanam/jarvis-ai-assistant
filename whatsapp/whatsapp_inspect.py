from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir="whatsapp_profile",
        headless=False,
    )

    page = context.new_page()
    page.goto("https://web.whatsapp.com")

    input("Open any chat and press Enter...")

    print("\n========== PAGE TITLE ==========")
    print(page.title())

    print("\n========== PAGE URL ==========")
    print(page.url)

    print("\n========== FIRST 5000 CHARACTERS ==========\n")
    print(page.content()[:5000])

    input("\nPress Enter to close...")

    context.close()
