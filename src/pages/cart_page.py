from playwright.sync_api import Page


class CartPage:
    def __init__(self, config: dict, page: Page):
        self.config = config
        self.page = page
        self.checkout_button = self.page.get_by_role(
            "button", name="Check out")

    def proceed_to_checkout(self):
        self.checkout_button.click()
