import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from utils.utilities import Utilities


class CheckoutPage:
    # Locators
    str_pay_with_card = "//button//span[text()='Pay with Card']"
    str_stripe_frame_name = "stripe_checkout_app"
    str_pay_with_card_button = "//span[contains(text(),'Pay')]//ancestor::button"
    str_input_placeholder = "//input[@placeholder='<text_replace>']"
    str_pay_INR = "//span[contains(text(),'Pay INR ₹')]"
    str_payment_success = "//p[contains(text(),'Your payment was successful')]"

    def __init__(self):
        self.obj_utilities = Utilities()

    # Action Methods
    def pay_with_card(self, file_name):
        """Processes payment by reading payment testdata from payment.json file"""
        try:
            pytest.driver.find_element_by_xpath(self.str_pay_with_card_button).click()
            pytest.driver.switch_to.frame(self.str_stripe_frame_name)
            wait = WebDriverWait(pytest.driver, 10)
            wait.until(ec.visibility_of_element_located((By.XPATH, self.str_pay_INR)))
            payment_data = self.obj_utilities.get_test_data(file_name)

            # Json's testdata values first part is equal to placeholders of the text field so we'll use them to identify fields
            # This is done to fill the form using a loop with fewer statements
            # Seperate entries are kept for different parts of card number because of strip's implementation we cant enter at once
            for data in payment_data:
                text = payment_data[data].split(';')
                wait.until(ec.visibility_of_element_located(
                    (By.XPATH, self.str_input_placeholder.replace("<text_replace>", text[0]))))
                pytest.driver.find_element_by_xpath(
                    self.str_input_placeholder.replace("<text_replace>", text[0])).click()
                pytest.driver.find_element_by_xpath(
                    self.str_input_placeholder.replace("<text_replace>", text[0])).send_keys(text[1])
                time.sleep(2)
            pytest.driver.find_element_by_xpath(self.str_pay_with_card_button).click()
            pytest.driver.switch_to.default_content()
        except:
            assert False, "Failed to pay with card"

    def verify_payment_status(self):
        """Verify if Payment success heading exists then assert it true, otherwise on exception it will assert False"""
        try:
            while WebDriverWait(pytest.driver, 20).until(
                    ec.url_to_be("https://weathershopper.pythonanywhere.com/confirmation")) is None:
                WebDriverWait(pytest.driver, 10).until(
                    ec.visibility_of_element_located((By.XPATH, self.str_payment_success)))
            pytest.driver.find_element_by_xpath(self.str_payment_success)
            assert True
        except:
            assert False, "Payment verification failed"
