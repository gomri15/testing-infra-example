from dataclasses import dataclass
import time
from typing import List
from core.config_models import Config
from core.product import Product, ProductVariant

from playwright.sync_api import Page, expect


@dataclass
class CartItem:
    product: Product
    variant: ProductVariant
    quantity: int


class Cart:
    def __init__(self, config: Config,  page: Page):
        self.page = page
        self.config = config
        self.items: List[CartItem] = []

    def add(self, product: Product, variant_enum, quantity: int):
        """
        Add an item to the cart.
        This method handles both selecting the variant in the UI and tracking the item.
        """
        variant = product.variants[variant_enum]
        self.page.locator("label").get_by_text(
            variant.name, exact=True).click()
        self.page.get_by_label("Quantity").fill(str(quantity))
        self.page.get_by_role("button", name="Add to cart").click()
        self.page.get_by_role("button", name="Continue shopping").click()
        self.items.append(
            CartItem(product=product, variant=variant, quantity=quantity))

    def calculate_total(self) -> float:
        """Calculate the total price of items in the cart."""
        return sum(item.variant.price * item.quantity for item in self.items)

    def assert_total_cart(self):
        """Verify the total amount in the UI matches the calculated total."""
        expected_total = self.calculate_total()
        formated_total = f"{expected_total:.2f}"
        self.page.pause()
        total_element = self.page.get_by_text(f"£{formated_total} GBP")
        total_element.scroll_into_view_if_needed()
        total_element.wait_for(state="visible")
        self.page.screenshot(path="cart.png")
        expect(total_element).to_be_visible(timeout=15000)

    def assert_total_checkout(self):
        """Verify the total amount in the UI matches the calculated total."""
        expected_total = self.calculate_total(
        ) + self.config.payment_information.shipping_cost
        formated_total = f"{expected_total:.2f}"
        self.page.get_by_label("Cost summary").get_by_text(f"{formated_total}")

    def total_quantity(self) -> int:
        """Calculate the total quantity of items in the cart."""
        return sum(item.quantity for item in self.items)

    def click_cart(self):
        """Click the checkout button in the cart."""
        self.page.get_by_role(
            "link", name=f"Cart {self.total_quantity()} items").click()
