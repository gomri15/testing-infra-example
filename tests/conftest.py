import pytest
import json
import os
from core.dropit import DropIt
from core.config_models import Config
from core.config_loader import load_config


def load_config(env: str) -> Config:

    config_path = os.path.join(os.path.dirname(
        __file__), f"..\src\config\config_{env}.json")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path) as config_file:
        config_data = json.load(config_file)

    # Add environment variable overrides if needed
    config_data["credentials"]["password"] = os.getenv(
        "PASSWORD", config_data["credentials"].get("password")
    )

    return Config(**config_data)


@pytest.fixture(scope="session")
def config(pytestconfig):
    env = pytestconfig.getoption("env") or "dev"
    return load_config(env)


@pytest.fixture
def dropit(config, context, page):
    """
    Initialize DropIt with Playwright's context and page fixtures.
    """
    return DropIt(config, context, page)


def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     default="dev",
                     help="Specify the test environment (e.g., dev, staging, production)"
                     )
    parser.addoption("--playwright-debug",
                     action="store_true",
                     help="Enable Playwright debug mode")


@pytest.fixture(scope="session", autouse=True)
def enable_debug_mode(request):
    if request.config.getoption("--playwright-debug"):
        os.environ["PWDEBUG"] = "1"


@pytest.fixture
def setup(dropit: DropIt):
    """
    Reset the application state before each test:
    - Log in
    - Clear the cart
    """
    dropit.goto("login_page")
    dropit.login_page.login()
    dropit.cart.items.clear()
