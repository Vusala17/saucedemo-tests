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


@pytest.mark.tags("JIRA-1", "ui", "products")
@pytest.mark.parametrize("products_page", ["standard_user"], indirect=True)
def test_product_list_and_sort(products_page):
    page=products_page
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"item-4-title-link\"] [data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Backpack")
    expect(page.locator("[data-test=\"item-0-title-link\"] [data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Bike Light")
    expect(page.locator("[data-test=\"item-1-title-link\"] [data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Bolt T-Shirt")
    expect(page.locator("[data-test=\"item-5-title-link\"] [data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Fleece Jacket")
    expect(page.locator("[data-test=\"item-2-title-link\"] [data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Onesie")
    expect(page.locator("[data-test=\"item-3-title-link\"] [data-test=\"inventory-item-name\"]")).to_contain_text("Test.allTheThings() T-Shirt (Red)")
    expect(page.locator("[data-test=\"inventory-list\"]")).to_contain_text("$29.99")
    expect(page.locator("[data-test=\"inventory-list\"]")).to_contain_text("$9.99")
    expect(page.locator("[data-test=\"inventory-list\"]")).to_contain_text("$15.99")
    expect(page.locator("[data-test=\"inventory-list\"]")).to_contain_text("$49.99")
    expect(page.locator("[data-test=\"inventory-list\"]")).to_contain_text("$7.99")
    expect(page.locator("[data-test=\"inventory-list\"]")).to_contain_text("$15.99")
    page.get_by_text("Name (A to Z)Name (A to Z)").click()
    page.locator("[data-test=\"product-sort-container\"]").select_option("lohi")
    page.get_by_text("Price (low to high)Name (A to").click()
    page.locator("[data-test=\"product-sort-container\"]").select_option("hilo")
