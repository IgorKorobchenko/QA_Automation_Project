import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("start-maximized")
    options.headless = False
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()