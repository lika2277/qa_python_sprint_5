import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import User, Url
from locators import entrance, links, buttons, account, main

user = User()
url = Url()

email, password = user.get_credentials().values()

def test_constructor_switch_sauce(browser):
    browser.get(url.get_url())

    # Клик по кнопке "Личный кабинет"
    browser.find_element(By.XPATH, links.get('account')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, buttons.get('enter'))))

    # Ввод "Email"
    browser.find_element(By.XPATH, entrance.get('inputs').get('email')).send_keys(email)

    # Ввод "Пароль"
    browser.find_element(By.XPATH, entrance.get('inputs').get('password')).send_keys(password)

    # Клик по кнопке "Войти"
    browser.find_element(By.XPATH, buttons.get('enter')).click()

    # Ожидание открытия главного экрана
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, links.get('account'))))

    # Клик по кнопке "Личный кабинет"
    browser.find_element(By.XPATH, links.get('account')).click()

    # Ожидание открытия личного кабинета
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, account.get('email'))))

    browser.find_element(By.XPATH, '//nav/div/a[@href="/"]').click()

    # Ожидание открытия главного экрана
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, main.get('buttons').get('order'))))

    assert browser.find_element(By.XPATH, main.get('buttons').get('order')).text == 'Оформить заказ'
