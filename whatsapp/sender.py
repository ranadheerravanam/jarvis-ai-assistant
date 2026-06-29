from playwright.sync_api import sync_playwright


class WhatsAppSender:

    def __init__(self):

        self.playwright = sync_playwright().start()

        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir="whatsapp_profile",
            headless=False,
        )

        self.page = self.context.new_page()

        self.page.goto("https://web.whatsapp.com")

        input("Open your own chat and press Enter...")

    def send(self, text):

        box = self.page.locator(
            'div[contenteditable="true"]'
        ).last

        box.click()

        box.fill(text)

        self.page.keyboard.press("Enter")
