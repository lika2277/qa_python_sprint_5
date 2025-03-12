import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from generator import Generator
from data import Url

class TestRegistration:

    @staticmethod
    def test_registration_form(browser):
        browser.get(Url().get_url())

        # Клик по кнопке "Личный кабинет"
        browser.find_element(By.CSS_SELECTOR, locators.link_account).click()

        # Ожидание показа формы входа
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.form_login)))

        # Клик по кнопке "Зарегистрироваться"
        browser.find_element(By.CSS_SELECTOR, locators.link_register).click()

        # Ожидание показа формы регистрации
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.form_login)))

        # Ввод "Имя"
        browser.find_element(By.CSS_SELECTOR, locators.field_name).send_keys("Лика")

        # Ввод "Email"
        email = Generator.generate_login("liliana_bubnova_19") + '@yandex.ru'
        browser.find_element(By.CSS_SELECTOR, locators.form_login + ' ' + locators.field_email).send_keys(email)

        # Ввод "Пароль"
        password = Generator.generate_password()
        browser.find_element(By.CSS_SELECTOR, locators.form_login + ' ' + locators.field_password).send_keys(password)

        # Клик по кнопке "Зарегистироваться"
        browser.find_element(By.XPATH, locators.button_register).click()

        # Ожидание показа формы входа
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.button_enter)))

        # Ввод "Email"
        browser.find_element(By.CSS_SELECTOR, locators.form_login + ' ' + locators.field_name).send_keys(email)

        # Ввод "Пароль"
        browser.find_element(By.CSS_SELECTOR, locators.form_login + ' ' + locators.field_password).send_keys(password)

        # Клик по кнопке "Войти"
        browser.find_element(By.XPATH, locators.button_enter).click()

        # Ожидание открытия главного экрана
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main_ingredients)))

        # Клик по кнопке "Личный кабинет"
        browser.find_element(By.CSS_SELECTOR, locators.link_account).click()

        # Ожидание открытия личного кабинета
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.page_account)))

        assert browser.find_element(By.CSS_SELECTOR, locators.page_account)


    @staticmethod
    def test_registration_error(browser):
        browser.get(Url().get_url())

        # Клик по кнопке "Личный кабинет"
        browser.find_element(By.CSS_SELECTOR, locators.link_account).click()

        # Ожидание показа формы входа
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.form_login)))

        # Клик по кнопке "Зарегистрироваться"
        browser.find_element(By.CSS_SELECTOR, locators.link_register).click()

        # Ожидание показа формы регистрации
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.form_login)))

        # Ввод "Имя"
        browser.find_element(By.CSS_SELECTOR, locators.field_name).send_keys("Лика")

        # Ввод "Email"
        email = Generator.generate_login("liliana_bubnova_19") + '@yandex.ru'
        browser.find_element(By.CSS_SELECTOR, locators.form_login + ' ' + locators.field_email).send_keys(
            email)

        # Ввод "Пароль"
        password = Generator.generate_password(0, 99999)
        browser.find_element(By.CSS_SELECTOR,
                             locators.form_login + ' ' + locators.field_password).send_keys(password)

        # Клик по кнопке "Зарегистироваться"
        browser.find_element(By.XPATH, locators.button_register).click()

        # Красная рамка вокруг поля "Пароль"
        error_input = browser.find_element(By.CSS_SELECTOR, locators.error_field)

        # Сообщение об ошибке
        error_message = browser.find_element(By.CSS_SELECTOR, locators.error_message)

        assert error_message and error_input