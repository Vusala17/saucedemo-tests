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


@pytest.mark.tags("JIRA-1", "ui", "checkout")
@pytest.mark.parametrize("products_page", ["standard_user"], indirect=True)
def test_standard_users_should_be_able_to_complete_checkout(products_page):
    page=products_page
    # Auto waiting
    # -------------
    # Ref: https://playwright.dev/python/docs/actionability
    products_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE).wait_for(state="visible", timeout=5000) # Explicit wait 
    products_page.wait_for_timeout(2000) # Explicit wait for 2 seconds (delay)
    
    expect(products_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(products_page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")

    page.locator(LOCATORS_PRODUCTS_PAGE_PRODUCT_NAME).click()
    page.locator(LOCATORS_CART_ICON).click()
    page.locator(LOCATOR_CHECKOUT_PAGE_CHECKOUT_BUTTON).click()
    page.locator(LOCATORS_CHECKOUT_PAGE_FIRSTNAME).click()
    page.locator(LOCATORS_CHECKOUT_PAGE_FIRSTNAME).fill(CONSTANT_CHECKOUT_PAGE_FIRSTNAME)
    page.locator(LOCATORS_CHECKOUT_PAGE_LASTNAME).click()
    page.locator(LOCATORS_CHECKOUT_PAGE_LASTNAME).fill(CONSTANT_CHECKOUT_PAGE_LASTNAME)
    page.locator(LOCATORS_CHECKOUT_PAGE_POSTALCODE).click()
    page.locator(LOCATORS_CHECKOUT_PAGE_POSTALCODE).fill(CONSTANT_CHECKOUT_PAGE_POSTALCODE)
    page.locator(LOCATORS_CHECKOUT_PAGE_CONTINUE).click()
    page.locator(LOCATORS_CHECKOUT_PAGE_FINISH).click()
    expect(page.locator(LOCATORS_SUCCESS_PAGE_HEADER)).to_contain_text(CONSTANT_SUCCESS_PAGE_HEADER)
