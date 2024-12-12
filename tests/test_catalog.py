import pytest
from core.dropit import DropIt
from core.product import CHIPS, HAMBURGER, ChipsVariant, HamburgerVariant
from playwright.sync_api import expect


def test_add_items_to_cart_and_checkout(dropit: DropIt, setup):
    dropit.catalog_page.go_to_product_page(HAMBURGER.name)
    dropit.cart.add(HAMBURGER, HamburgerVariant.EXTRA_LARGE, 1)
    dropit.cart.add(HAMBURGER, HamburgerVariant.LARGE, 2)

    dropit.catalog_page.go_to_product_page(CHIPS.name)
    dropit.cart.add(CHIPS, ChipsVariant.EXTRA_LARGE, 1)
    dropit.cart.add(CHIPS, ChipsVariant.LARGE, 2)

    dropit.cart.click_cart()
    dropit.cart_page.proceed_to_checkout()

    dropit.checkout_page.fill_user_details()
    dropit.checkout_page.fill_payment_details()
    dropit.cart.assert_total_checkout()

    dropit.checkout_page.submit_payment()
    dropit.page.get_by_role(
        "heading", name="Thank you!").is_visible(timeout=15000)


def test_invalid_payment_info_cant_checkout(dropit: DropIt, setup):

    dropit.catalog_page.go_to_product_page(HAMBURGER.name)
    dropit.cart.add(HAMBURGER, HamburgerVariant.EXTRA_LARGE, 1)
    dropit.catalog_page.click_buy_now()

    dropit.checkout_page.fill_email(email="invalid_email")
    dropit.checkout_page.fill_card_number(card_number="777")
    dropit.checkout_page.submit_payment()
    dropit.checkout_page.validate_errors()
    expect(dropit.page.get_by_role(
        "heading", name="Thank you!")).not_to_be_visible()
