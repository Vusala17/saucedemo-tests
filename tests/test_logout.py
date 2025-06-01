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

# pytest tests/test_logout.py -v --tags JIRA-3 --browser=chromium --slowmo 500 --headed --html=report.html
@pytest.mark.tags("JIRA-3", "ui", "logout")
@pytest.mark.parametrize("products_page", ["standard_user"], indirect=True)
def test_logout_from_hamburger_menu(products_page):
    page=products_page
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    expect(page.locator("[data-test=\"login-button\"]")).to_be_visible()
