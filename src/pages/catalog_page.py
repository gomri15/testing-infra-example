from playwright.sync_api import Page, expect


class CatalogPage:
    def __init__(self, config: dict, page: Page):
        self.config = config
        self.page = page
        self.search_button = self.page.get_by_role("button", name="Search")
        self.search_input = self.page.get_by_role("combobox", name="Search")

    def click_buy_now(self):
        """Click the Buy now button on the product page."""
        self.page.get_by_role("button", name="Buy it now").click()

    def go_to_product_page(self, product_name: str, verify: bool = True):
        """
        Search for a product by name, navigate to its page, handle scrolling issues,
        and optionally verify that the navigation was successful.

        :param product_name: The name of the product to search for.
        :param verify: Whether to verify the navigation (default: True).
        """
        # Perform product search
        self.search_button.scroll_into_view_if_needed()
        self.search_button.click()
        self.search_input.scroll_into_view_if_needed()
        self.search_input.click()
        self.search_input.fill(product_name)

        # Navigate to the product page
        search_result = self.page.get_by_role("link", name=product_name)
        search_result.scroll_into_view_if_needed()
        search_result.click()

        # Optionally verify successful navigation
        if verify:
            header = self.page.get_by_role("heading", name=product_name)
            header.scroll_into_view_if_needed()
            expect(header).to_be_visible(timeout=5000)