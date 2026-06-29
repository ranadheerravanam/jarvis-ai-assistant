from playwright.sync_api import sync_playwright


class WhatsAppReader:

    def __init__(self):

        self.playwright = sync_playwright().start()

        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir="whatsapp_profile",
            headless=False,
        )

        self.page = self.context.new_page()

        self.page.goto("https://web.whatsapp.com")

        input("Open your own chat and press Enter...")

    def latest_message(self):

        messages = self.page.locator(
            "div.copyable-text span.selectable-text"
        )

        count = messages.count()

        if count == 0:
            return None

        return messages.nth(count - 1).inner_text().strip()
