import pytest


class Homepage:

    # Locators
    temperature = "//span[@id='temperature']"
    btn_products = "//button[contains(text(),'<text_replace>')]"

    # Temperature threshold
    low_temp_threshold = 19
    high_temp_threshold = 34
    product_key_moisturizers = "moisturizers"
    product_key_sunscreens = "sunscreens"

    def read_temperature(self):
        """This method reads temperature from homepage"""
        try:
            return int(pytest.driver.find_element_by_xpath(self.temperature).text.split(' ')[0])
        except:
            assert False

    def choose_product_type(self, int_temperature):
        """Click on the appropriate product type based on temperature"""
        try:
            if int_temperature < self.low_temp_threshold:
                pytest.driver.find_element_by_xpath(self.btn_products.replace("<text_replace>", self.product_key_moisturizers)).click()
                return self.product_key_moisturizers

            elif int_temperature > self.high_temp_threshold:
                pytest.driver.find_element_by_xpath(self.btn_products.replace("<text_replace>", self.product_key_sunscreens)).click()
                return self.product_key_sunscreens
            else:
                pytest.driver.quit()
        except:
            assert False


