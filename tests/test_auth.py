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


@pytest.mark.tags("JIRA-0001", "ui", "auth")
@pytest.mark.parametrize("products_page", ["standard_user"], indirect=True)
def test_standard_users_should_be_able_to_see_products(products_page):
    # Auto waiting
    # -------------
    # Ref: https://playwright.dev/python/docs/actionability
    products_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE).wait_for(state="visible", timeout=5000) # Explicit wait 
    products_page.wait_for_timeout(2000) # Explicit wait for 2 seconds (delay)
    
    expect(products_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(products_page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")

# pytest tests/test_auth.py -v --tags JIRA-0002 --browser=chromium --slowmo 500 --headed --html=report.html

@pytest.mark.tags("JIRA-0002", "ui", "auth")
@pytest.mark.parametrize("products_page", ["problem_user"], indirect=True)
def test_problem_users_should_be_able_to_see_products(products_page):
    products_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE).wait_for(state="visible", timeout=5000) # Explicit wait 
    expect(products_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(products_page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")


@pytest.mark.tags("JIRA-0003", "ui", "auth")
@pytest.mark.parametrize("products_page", ["locked_out_user"], indirect=True)
def test_locked_out_users_should_not_be_able_to_see_products(products_page):
    expect(products_page.locator(LOCATORS_AUTH_ERROR_MESSAGE)).to_have_text(CONSTANTS_AUTH_ERROR_MESSAGE)
    expect(products_page).to_have_url(CONSTANTS_START_URL)


@pytest.mark.tags("JIRA-0004", "ui", "auth")
@pytest.mark.parametrize("products_page", ["performance_glitch_user"], indirect=True)
def test_performance_glitch_users_should_be_able_to_see_products(products_page):
    products_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE).wait_for(state="visible", timeout=5000) # Explicit wait 
    expect(products_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(products_page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")


@pytest.mark.tags("JIRA-0005", "ui", "auth")
@pytest.mark.parametrize("products_page", ["error_user"], indirect=True)
def test_error_users_should_be_able_to_see_products(products_page):
    products_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE).wait_for(state="visible", timeout=5000) # Explicit wait 
    expect(products_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(products_page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")


@pytest.mark.tags("JIRA-0006", "ui", "auth")
@pytest.mark.parametrize("products_page", ["visual_user"], indirect=True)
def test_visual_users_should_be_able_to_see_products(products_page):
    products_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE).wait_for(state="visible", timeout=5000) # Explicit wait 
    expect(products_page.locator(LOCATORS_PRODUCTS_PAGE_TITLE)).to_have_text(CONSTANTS_PRODUCTS_PAGE_TITLE)
    expect(products_page).to_have_url(f"{CONSTANTS_BASE_URL}/inventory.html")


# Yanlış istifadəçi adı/parolla girişin mümkün olmamasını yoxlayın (xətanın göstərilməsi).
# pytest tests/test_auth.py -v --tags JIRA-0007 --browser=chromium --slowmo 500 --headed --html=report.html
@pytest.mark.tags("JIRA-0007", "ui", "auth" ,"negative")
def test_unregistered_user_shouldnt_be_able_to_login(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("vusala")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("12345")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username and password do not match any user in this service")


# locked_out_user ilə girişin bloklanmasını test edin.
# pytest tests/test_auth.py -v --tags JIRA-0008 --browser=chromium --slowmo 500 --headed --html=report.html
@pytest.mark.tags("JIRA-0008", "ui", "auth" ,"negative")
def test_locked_out_user_is_blocked(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("locked_out_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Sorry, this user has been locked out.")
    
