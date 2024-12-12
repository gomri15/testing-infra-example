from typing import Optional
from core.config_models import Config
from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, config: Config, page: Page):
        self.page = page
        self.config = config
        self.email_input = self.page.get_by_placeholder(
            "Email or mobile phone number")
        self.last_name_input = self.page.get_by_placeholder("Last name")
        self.address_input = self.page.get_by_placeholder("Address")
        self.city_input = self.page.get_by_placeholder("City")
        self.expiry_input = self.page.locator(
            "iframe[name^=card-fields-expiry]").content_frame.get_by_placeholder("Expiration date (MM / YY)")
        self.cvv_input = self.page.locator(
            "iframe[name^=card-fields-verification_value]").content_frame.get_by_placeholder("Security code")
        self.card_name_input = self.page.locator(
            "iframe[name^=card-fields-name]").content_frame.get_by_placeholder("Name on card")
        self.card_number_input = self.page.locator(
            "iframe[name^=card-fields-number]").content_frame.get_by_placeholder("Card number")
        self.pay_now_button = self.page.get_by_role("button", name="Pay now")

    def fill_last_name(self, last_name: Optional[str] = None):
        self.last_name_input.fill(
            last_name or self.config.user_details.last_name)

    def fill_address(self, address: Optional[str] = None):
        self.address_input.fill(address or self.config.user_details.address)

    def fill_city(self, city: Optional[str] = None):
        self.city_input.fill(city or self.config.user_details.city)

    def fill_email(self, email: Optional[str] = None):
        self.email_input.fill(email or self.config.user_details.email)

    def fill_expiry(self, expiry: Optional[str] = None):
        self.expiry_input.fill(expiry or self.config.payment_details.expiry)

    def fill_cvv(self, cvv: Optional[str] = None):
        self.cvv_input.fill(cvv or self.config.payment_details.cvv)

    def fill_card_name(self, name_on_card: Optional[str] = None):
        self.card_name_input.fill(
            name_on_card or self.config.payment_details.name_on_card)

    def fill_card_number(self, card_number: Optional[str] = None):
        self.card_number_input.fill(
            card_number or self.config.payment_details.card_number)

    def fill_user_details(self,
                          email: Optional[str] = None,
                          last_name: Optional[str] = None,
                          address: Optional[str] = None,
                          city: Optional[str] = None):
        self.fill_email(email)
        self.fill_last_name(last_name)
        self.fill_address(address)
        self.fill_city(city)

    def fill_payment_details(self,
                             expiry: Optional[str] = None,
                             cvv: Optional[str] = None,
                             name_on_card: Optional[str] = None,
                             card_number: Optional[str] = None):
        self.fill_expiry(expiry)
        self.fill_cvv(cvv)
        self.fill_card_name(name_on_card)
        self.fill_card_number(card_number)

    def submit_payment(self):
        self.pay_now_button.click()
        if self.page.get_by_text("Payment successful").is_visible():
            raise RuntimeError(
                "Payment should not have been successful with invalid data.")

    def validate_errors(self) -> dict:
        return {
            "email_error": self.email_input.get_attribute("aria-invalid") == "true",
            "expiry_error": self.expiry_input.get_attribute("aria-invalid") == "true",
        }
