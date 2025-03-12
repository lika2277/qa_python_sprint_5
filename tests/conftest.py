import pytest
import locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import Url, Constructor

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope = 'function')
def page(browser):
    browser.get(Url().get_url())

    return Constructor(
        browser.find_elements(By.CSS_SELECTOR, locators.constructor_tab),
        browser.find_elements(By.CSS_SELECTOR, locators.constructor_heading)
    )