from pydantic import BaseModel


class URLs(BaseModel):
    base: str
    login_page: str
    catalog_page: str
    pets: str


class Credentials(BaseModel):
    username: str
    password: str


class UserDetails(BaseModel):
    email: str
    last_name: str
    address: str
    city: str


class PaymentDetails(BaseModel):
    expiry: str
    cvv: str
    name_on_card: str
    card_number: str

class PaymentInformation(BaseModel):
    shipping_cost: float

class Config(BaseModel):
    urls: URLs
    credentials: Credentials
    user_details: UserDetails
    payment_details: PaymentDetails
    payment_information: PaymentInformation
