import pytest
import locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from data import urls

class Constructor:
    def __init__(self, tabs: list[WebElement], headings: list[WebElement]):
        self.tabs = tabs
        self.headings = headings

    def get_tab(self, value = ''):
        if not property or not value:
            return None

        for tab in self.tabs:
            if tab.get_property('innerText') == value:
                return tab

    def get_heading(self, value= ''):
        if not property or not value:
            return None

        for heading in self.headings:
            if heading.get_property('innerText') == value:
                return heading

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope = 'function')
def page(browser):
    browser.get(urls.get('main'))

    return Constructor(
        browser.find_elements(By.CSS_SELECTOR, locators.constructor_tab),
        browser.find_elements(By.CSS_SELECTOR, locators.constructor_heading)
    )