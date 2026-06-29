from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir="whatsapp_profile",
        headless=False,
    )

    page = context.new_page()

    page.goto("https://web.whatsapp.com")

    print("Scan the QR code if needed.")
    input("After your chats are fully loaded, press Enter...")

    print("✅ Profile saved successfully!")

    context.close()
