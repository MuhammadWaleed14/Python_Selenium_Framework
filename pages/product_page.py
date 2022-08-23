import pytest


class ProductPage:

    # Locators
    str_product = "//p[contains(text(), '<text_replace>')]//parent::div//p[contains(text(),'Price')]//following-sibling::button"
    str_button_cart = "//span[@id='cart']//parent::button"

    def select_product(self, str_product_name):
        """
        This method is used to select Products
        :return: none
        """
        try:
            pytest.driver.find_element_by_xpath(self.str_product.replace("<text_replace>", str_product_name)).click()
        except:
            assert False

    def go_to_cart(self):
        """Click on Cart button"""
        try:
            pytest.driver.find_element_by_xpath(self.str_button_cart).click()
        except:
            assert False



