from playwright.sync_api import sync_playwright


class BrowserManager:

    def __init__(self):

        self.playwright = sync_playwright().start()

        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir="whatsapp/whatsapp_profile",
            headless=False,
        )

        self.page = self.context.new_page()

    def close(self):

        self.context.close()

        self.playwright.stop()
