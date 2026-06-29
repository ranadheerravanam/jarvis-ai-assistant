from browser.browser_manager import BrowserManager


class WhatsAppManager:

    def __init__(self):

        self.browser = BrowserManager()

        self.page = self.browser.page

        self.page.goto("https://web.whatsapp.com")

        input("Open your own chat and press Enter...")

    def latest_message(self):

        messages = self.page.locator(
            "div.copyable-text span.selectable-text"
        )

        if messages.count() == 0:
            return None

        return messages.nth(
            messages.count() - 1
        ).inner_text()

    def send(self, text):

        box = self.page.locator(
            'div[contenteditable="true"]'
        ).last

        box.click()

        box.fill(text)

        self.page.keyboard.press("Enter")
