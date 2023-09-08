import time

from pages.base_page import URL
from pages.elements_page import TextBoxPage


class TestElements:
    class TestBox:

        def test_test_box(self, driver):
            text_box_page = TextBoxPage(driver, URL)
            text_box_page.open()
            text_box_page.fill_all_fields()
            time.sleep(5)
