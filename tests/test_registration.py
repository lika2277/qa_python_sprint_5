import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from generator import Generator
from data import Url
from locators import links, buttons, entrance, account, fields

url = Url()

def test_constructor_switch_sauce(browser):
    browser.get(url.get_url())

    # Переход на страницу авторизации
    # Клик по кнопке "Личный кабинет"
    browser.find_element(By.XPATH, links.get('account')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, links.get('register'))))

    # Переход на форму регистрации
    # Клик по кнопке "Зарегистрироваться"
    browser.find_element(By.XPATH, links.get('register')).click()

    # Ожидание показа формы регистрации
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, buttons.get('register'))))

    # Ввод данных дял регистрации
    # Ввод "Имя"
    browser.find_element(By.XPATH, fields.get('registration').get('name')).send_keys("Лика")

    # Ввод "Email"
    email = Generator.generate_login("liliana_bubnova_19") + '@yandex.ru'
    browser.find_element(By.XPATH, fields.get('registration').get('email')).send_keys(email)

    # Ввод "Пароль"
    password = Generator.generate_password()
    browser.find_element(By.XPATH, entrance.get('inputs').get('password')).send_keys(password)

    # Клик по кнопке "Зарегистироваться"
    browser.find_element(By.XPATH, buttons.get('register')).click()

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

    # Переход в личный кабинет
    browser.find_element(By.XPATH, links.get('account')).click()

    # Ожидание открытия личного кабинета
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, account.get('email'))))

    # Получить значение логина
    login = browser.find_element(By.XPATH, account.get('email')).get_attribute('value')

    assert login == email