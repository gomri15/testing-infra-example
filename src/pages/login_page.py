from playwright.sync_api import Page

from core.config_models import Config

class LoginPage:
    def __init__(self, config: Config, page: Page):
        self.config = config
        self.page = page
        self.password_input = self.page.get_by_label("Enter store password")
        self.enter_button = self.page.get_by_role("button", name="Enter")

    def login(self):
        try:
            self.password_input.click()
            self.password_input.fill(self.config.credentials.password)
            self.enter_button.click()
        except Exception as e:
            raise RuntimeError(f"Login failed: {e}")
