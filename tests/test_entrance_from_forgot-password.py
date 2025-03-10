import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import User, Url
from locators import main, entrance, buttons, links

user = User()
url = Url()

email, password = user.get_credentials().values()

def test_constructor_switch_sauce(browser):
    browser.get(url.get_url('forgot'))

    # Клик по кнопке "Войти"
    browser.find_element(By.XPATH, links.get('login')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, buttons.get('enter'))))

    # Ввод "Email"
    browser.find_element(By.XPATH, entrance.get('inputs').get('email')).send_keys(email)

    # Ввод "Пароль"
    browser.find_element(By.XPATH, entrance.get('inputs').get('password')).send_keys(password)

    # Клик по кнопке "Войти"
    browser.find_element(By.XPATH, buttons.get('enter')).click()

    # Ожидание открытия главного экрана
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, main.get('buttons').get('order'))))

    assert browser.find_element(By.XPATH, main.get('buttons').get('order')).text == 'Оформить заказ'
