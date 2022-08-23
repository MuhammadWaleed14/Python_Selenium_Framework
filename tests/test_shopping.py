import pytest
from pytest_bdd import (given, when, scenario, then, parsers)
from pages.Homepage import Homepage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage
from utils.utilities import Utilities

obj_homepage = Homepage()
obj_utilities = Utilities()
obj_product_page = ProductPage()
int_temperature = None
obj_checkout_page = CheckoutPage()


@scenario(r'features/shopping.feature', 'Purchase sunscreens for high temperature and moisturisers for low temperature')
def test_purchase_sunscreens_for_high_temperature_and_moisturisers_for_low_temperature():
    """Purchase sunscreens for high temperature and moisturisers for low temperature."""


@given(parsers.cfparse('User navigates to "{url}"'))
def user_navigates_to_(url):
    """User navigates to ""."""
    pytest.driver.get(url)


@when('User navigates to Cart')
def user_navigates_to_cart():
    """User navigates to Cart"""
    obj_product_page.go_to_cart()


@when(parsers.cfparse('User pays with card using payment information from "{file_name}"'))
def user_pays_with_card(file_name):
    """User pays with card."""
    obj_checkout_page.pay_with_card(file_name)


@when(parsers.cfparse('User reads temperature and purchases products mentioned in "{file_name}"'))
def user_purchases_the_products(file_name):
    """User purchases the products
    """
    try:
        int_temp = obj_homepage.read_temperature()
        str_product_type = obj_homepage.choose_product_type(int_temperature=int_temp)
        dict_products = obj_utilities.get_test_data(file_name)[str_product_type]
        for product in dict_products:
            obj_product_page.select_product(str(product))
    except:
        assert False, "Navigation from homepage to product page failed"


@then('Verify that user is able to make payment successfully')
def verify_that_user_is_able_to_make_payment_successfully():
    """Verify that user is able to make payment successfully."""
    obj_checkout_page.verify_payment_status()

