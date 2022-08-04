import pytest
from configuration import *
from selenium import webdriver


class TestBrowser:
    def __init__(self, options, executable_path):
        self.options = options
        self.executable_path = executable_path

    def driver(self):
        driver = webdriver.Chrome(options=self.options, executable_path=self.executable_path)
        return driver


@pytest.fixture(scope='session')
def base():
    driver = TestBrowser(options=OPTIONS, executable_path=PATH).driver()   # and TestBrowser.driver_get

    yield driver

    driver.quit()
