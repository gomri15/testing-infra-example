from dataclasses import dataclass
from enum import Enum
from typing import Dict


@dataclass
class ProductVariant:
    name: str
    price: float


@dataclass
class Product:
    name: str
    variants: Dict[Enum, ProductVariant]


class HamburgerVariant(Enum):
    LARGE = "Large"
    EXTRA_LARGE = """So large you can't eat it"""


class ChipsVariant(Enum):
    LARGE = "Large"
    EXTRA_LARGE = "Too much for you to handle"


HAMBURGER = Product(
    name="Dropit Hamburger (QA Automation)",
    variants={
        HamburgerVariant.LARGE: ProductVariant(name=HamburgerVariant.LARGE.value, price=7.00),
        HamburgerVariant.EXTRA_LARGE: ProductVariant(name=HamburgerVariant.EXTRA_LARGE.value, price=9.00),
    },
)

CHIPS = Product(
    name="Dropit Chips (QA Automation)",
    variants={
        ChipsVariant.LARGE: ProductVariant(name=ChipsVariant.LARGE.value, price=3.00),
        ChipsVariant.EXTRA_LARGE: ProductVariant(name=ChipsVariant.EXTRA_LARGE.value, price=4.00),
    },
)
