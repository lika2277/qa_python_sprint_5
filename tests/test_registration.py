import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from generator import Generator
from data import Url

def test_registration_form(browser):
    browser.get(Url().get_url())

    # Клик по кнопке "Личный кабинет"
    browser.find_element(By.CSS_SELECTOR, locators.links.get('account')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.forms.get('login'))))

    # Клик по кнопке "Зарегистрироваться"
    browser.find_element(By.CSS_SELECTOR, locators.links.get('register')).click()

    # Ожидание показа формы регистрации
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.forms.get('login'))))

    # Ввод "Имя"
    browser.find_element(By.CSS_SELECTOR, locators.fields.get('name')).send_keys("Лика")

    # Ввод "Email"
    email = Generator.generate_login("liliana_bubnova_19") + '@yandex.ru'
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('email')).send_keys(email)

    # Ввод "Пароль"
    password = Generator.generate_password()
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('password')).send_keys(password)

    # Клик по кнопке "Зарегистироваться"
    browser.find_element(By.XPATH, locators.buttons.get('register')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.buttons.get('enter'))))

    # Ввод "Email"
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('name')).send_keys(email)

    # Ввод "Пароль"
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('password')).send_keys(password)

    # Клик по кнопке "Войти"
    browser.find_element(By.XPATH, locators.buttons.get('enter')).click()

    # Ожидание открытия главного экрана
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main.get('ingredients'))))

    # Клик по кнопке "Личный кабинет"
    browser.find_element(By.CSS_SELECTOR, locators.links.get('account')).click()

    # Ожидание открытия личного кабинета
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.page.get('account'))))

    assert browser.find_element(By.CSS_SELECTOR, locators.page.get('account'))


def test_registration_error(browser):
    browser.get(Url().get_url())

    # Клик по кнопке "Личный кабинет"
    browser.find_element(By.CSS_SELECTOR, locators.links.get('account')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.forms.get('login'))))

    # Клик по кнопке "Зарегистрироваться"
    browser.find_element(By.CSS_SELECTOR, locators.links.get('register')).click()

    # Ожидание показа формы регистрации
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.forms.get('login'))))

    # Ввод "Имя"
    browser.find_element(By.CSS_SELECTOR, locators.fields.get('name')).send_keys("Лика")

    # Ввод "Email"
    email = Generator.generate_login("liliana_bubnova_19") + '@yandex.ru'
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('email')).send_keys(
        email)

    # Ввод "Пароль"
    password = Generator.generate_password(0, 99999)
    browser.find_element(By.CSS_SELECTOR,
                         locators.forms.get('login') + ' ' + locators.fields.get('password')).send_keys(password)

    # Клик по кнопке "Зарегистироваться"
    browser.find_element(By.XPATH, locators.buttons.get('register')).click()

    # Красная рамка вокруг поля "Пароль"
    error_input = browser.find_element(By.CSS_SELECTOR, locators.errors.get('field'))

    # Сообщение об ошибке
    error_message = browser.find_element(By.CSS_SELECTOR, locators.errors.get('message'))

    assert error_message and error_input