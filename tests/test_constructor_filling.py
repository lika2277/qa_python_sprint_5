import pytest
from time import sleep
from selenium.webdriver.common.by import By
from data import Url
from locators import constructor

url = Url()

def test_constructor_switch_filling(browser):
    browser.get(url.get_url())

    # Расчет позиции первой категории (так как она первая по-умолчанию)
    y = int(browser.find_element(By.XPATH, constructor.get('sections').get('bread')).rect.get('y'))

     # Нажатие на кнопку "Начинки"
    browser.find_element(By.XPATH, constructor.get('tabs').get('filling')).click()

    # Ожидание анимации
    sleep(1)

    # Проверка прокрутки до начала области просмотра
    assert int(browser.find_element(By.XPATH, constructor.get('sections').get('filling')).rect.get('y')) <= y