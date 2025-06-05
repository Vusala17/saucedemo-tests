# ===================================== #
# Locators
# Ref: https://playwright.dev/python/docs/locators
# Ref: https://playwright.dev/python/docs/api/class-locatorassertions#methods
# ===================================== #
LOCATORS_AUTH_USERNAME = "input#user-name"
LOCATORS_AUTH_PASSWORD = "input#password"
LOCATORS_AUTH_LOGIN_BTN = "input#login-button"
LOCATORS_AUTH_ERROR_MESSAGE = "h3[data-test=\"error\"]"
LOCATORS_PRODUCTS_PAGE_TITLE = "span[data-test=\"title\"]"
LOCATORS_PRODUCTS_PAGE_PRODUCT_NAME="[data-test=\"add-to-cart-sauce-labs-backpack\"]"
LOCATORS_PRODUCT_SAUCE_LABS_BACKPACK = "div.inventory_item_name:text('Sauce Labs Backpack')"
LOCATORS_PRODUCT_SAUCE_LABS_BIKE_LIGHT = "div.inventory_item_name:text('Sauce Labs Bike Light')"
LOCATORS_PRODUCT_SAUCE_LABS_BOLT_T_SHIRT = "div.inventory_item_name:text('Sauce Labs Bolt T-Shirt')"
LOCATORS_PRODUCT_SAUCE_LABS_ONESIE = "div.inventory_item_name:text('Sauce Labs Onesie')"
LOCATORS_PRODUCT_SAUCE_LABS_FLEECE_JACKET = "div.inventory_item_name:text('Sauce Labs Fleece Jacket')"
LOCATORS_PRODUCT_TEST_ALL_THE_THINGS_T_SHIRT = "div.inventory_item_name:text('Test.allTheThings() T-Shirt (Red)')"
LOCATORS_ADD_TO_CART_BUTTON = "button:has-text('Add to cart')"
LOCATORS_CART_ICON="[data-test=\"shopping-cart-link\"]"
LOCATORS_REMOVE_FROM_CART_BUTTON = "button:has-text('Remove')"
LOCATOR_CHECKOUT_PAGE_CHECKOUT_BUTTON="[data-test=\"checkout\"]"
LOCATORS_CHECKOUT_PAGE_FIRSTNAME="[data-test=\"firstName\"]"
LOCATORS_CHECKOUT_PAGE_LASTNAME="[data-test=\"lastName\"]"
LOCATORS_CHECKOUT_PAGE_POSTALCODE="[data-test=\"postalCode\"]"
LOCATORS_CHECKOUT_PAGE_CONTINUE="[data-test=\"continue\"]"
LOCATORS_CHECKOUT_PAGE_FINISH="[data-test=\"finish\"]"
LOCATORS_SUCCESS_PAGE_HEADER="[data-test=\"complete-header\"]"

