import time

from locators.elements_page_locators import TextBoxLocators
from pages.base_page import BasePage



class TextBoxPage(BasePage):
    locators = TextBoxLocators

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys("Carl Cox")
        self.element_is_visible(self.locators.EMAIL).send_keys("CarlCox@gmail.com")
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys("2202 Magnolia st, LA, CA 90210")
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys("1234 Ohio st, Chicago, IL. 77888")
        self.element_is_visible(self.locators.SUBMIT).click()


