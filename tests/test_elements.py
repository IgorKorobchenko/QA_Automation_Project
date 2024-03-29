import random
import time

from pages.base_page import URL
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


class TestElements:
    class TestBox:

        def test_test_box(self, driver):
            text_box_page = TextBoxPage(driver, URL)
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_per_address = text_box_page.check_filled_form()
            time.sleep(10)
            assert full_name == output_name, "the full name doesn't match "
            assert email == output_email, "the email name doesn't match "
            assert current_address == output_current_address, "the current address name doesn't match "
            assert permanent_address == output_per_address, "the permanent address name doesn't match "

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, 'checkboxes have not been selected'

    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_radio_buttons('Yes')
            ouput_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_radio_buttons('Impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_radio_buttons('No')
            ouput_no = radio_button_page.get_output_result()
            assert ouput_yes == 'Yes', 'Yes has not been selected'
            assert output_impressive == 'Impressive', 'Impressive has not been selected'
            assert ouput_no == 'No', 'No has not been selected'

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            print(key_word)
            print(table_result)
            assert key_word in table_result







