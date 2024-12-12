from playwright.sync_api import Page


class ProductPage:
    def __init__(self, config: dict, page: Page):
        self.config = config
        self.page = page

    def select_variant(self, variant_name: str):
        self.page.get_by_text(variant_name).click()

    def increase_quantity(self):
        self.page.get_by_role(
            "button", name="Increase quantity for Dropit").click()

    def add_to_cart(self):
        self.page.get_by_role("button", name="Add to cart").click()
        if not self.page.get_by_text("added to cart").is_visible():
            raise RuntimeError("Failed to add product to cart.")
