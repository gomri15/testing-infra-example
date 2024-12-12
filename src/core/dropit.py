from backend.api.pets_api_client import PetsApiClient
from core.cart import Cart
from core.config_models import Config
from core.dropit_logger import setup_logger
from pages.cart_page import CartPage
from pages.catalog_page import CatalogPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from playwright.sync_api import Page, BrowserContext


class DropIt:
    def __init__(self, config: Config, context: BrowserContext, page: Page):
        self.config = config
        self.context = context
        self.page = page
        self.logger = setup_logger("DropIt Base")

        self.login_page = LoginPage(config, page)
        self.catalog_page = CatalogPage(config, page)
        self.product_page = ProductPage(config, page)
        self.cart_page = CartPage(config, page)
        self.checkout_page = CheckoutPage(config, page)
        self.cart = Cart(config, page)

        self.pets_api = PetsApiClient(
            page.context.request, self.config.urls.pets, self.logger)
        self.logger.info("DropIt initialized")

    def goto(self, url_key: str):
        url = getattr(self.config.urls, url_key, None)
        if not url:
            raise ValueError(f"URL for {url_key} not found in config")
        self.page.goto(url)
        if not self.page.url.startswith(url):
            raise RuntimeError(
                f"Failed to navigate to {url}. Current URL: {self.page.url}")
