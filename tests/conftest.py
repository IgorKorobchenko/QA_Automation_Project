import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


# @pytest.fixture(scope='function')
# def driver():
#     options = Options()
#     options.add_argument("start-maximized")
#     options.headless = False
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()

@pytest.fixture(scope='session')
def driver():
    options = Options()
    options.add_argument("start-maximized")
    options.headless = False
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()