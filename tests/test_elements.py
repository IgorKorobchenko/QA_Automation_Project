import time

from pages.base_page import URL
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


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





