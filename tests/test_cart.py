# ===================================== #
# Tests
# Ref: https://playwright.dev/python/docs/test-assertions
# ===================================== #
import pytest
from playwright.sync_api import expect
from data.constants import *
from data.locators import *
from fixtures.playwright import *
from fixtures.saucedemo import *

# pytest tests/test_cart.py -v --tags JIRA-2 --browser=chromium --slowmo 500 --headed --html=report.html
@pytest.mark.tags("JIRA-2", "ui", "cart")
@pytest.mark.parametrize("products_page", ["standard_user"], indirect=True)
def test_cart_functionality(products_page):
    page = products_page
    expect(page.locator("[data-test=\"item-5-title-link\"] [data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Fleece Jacket")
    page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Fleece Jacket")

