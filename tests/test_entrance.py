import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import User, Url

class TestEntrance:

    @staticmethod
    def test_entrance_from_cabinet(browser):
        browser.get(Url().get_url())

        email, password = User().get_credentials().values()

        # Клик по кнопке "Личный кабинет"
        browser.find_element(By.CSS_SELECTOR, locators.link_account).click()

        # Ожидание показа формы входа
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.form_login)))

        # Ввод "Email"
        browser.find_element(By.CSS_SELECTOR, locators.form_login + ' ' + locators.field_name).send_keys(email)

        # Ввод "Пароль"
        browser.find_element(By.CSS_SELECTOR, locators.form_login + ' ' + locators.field_password).send_keys(password)

        # Клик по кнопке "Войти"
        browser.find_element(By.XPATH, locators.button_enter).click()

        # Ожидание открытия главного экрана
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main_ingredients)))

        assert browser.find_element(By.CSS_SELECTOR, locators.main_ingredients)

    @staticmethod
    def test_entrance_from_forgot_password(browser):
        browser.get(Url().get_url('forgot'))

        email, password = User().get_credentials().values()

        # Клик по кнопке "Войти"
        browser.find_element(By.CSS_SELECTOR, locators.link_account).click()

        # Ожидание показа формы входа
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.form_login)))

        # Ввод "Email"
        browser.find_element(By.CSS_SELECTOR, locators.form_login + ' ' + locators.field_name).send_keys(email)

        # Ввод "Пароль"
        browser.find_element(By.CSS_SELECTOR, locators.form_login + ' ' + locators.field_password).send_keys(password)

        # Клик по кнопке "Войти"
        browser.find_element(By.XPATH, locators.button_enter).click()

        # Ожидание открытия главного экрана
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main_ingredients)))

        assert browser.find_element(By.CSS_SELECTOR, locators.main_ingredients)

    @staticmethod
    def test_entrance_from_main(browser):
        browser.get(Url().get_url())

        email, password = User().get_credentials().values()

        # Клик по кнопке "Войти"
        browser.find_element(By.CSS_SELECTOR, locators.link_account).click()

        # Ожидание показа формы входа
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.form_login)))

        # Ввод "Email"
        browser.find_element(By.CSS_SELECTOR, locators.form_login + ' ' + locators.field_name).send_keys(email)

        # Ввод "Пароль"
        browser.find_element(By.CSS_SELECTOR, locators.form_login + ' ' + locators.field_password).send_keys(password)

        # Клик по кнопке "Войти"
        browser.find_element(By.XPATH, locators.button_enter).click()

        # Ожидание открытия главного экрана
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main_ingredients)))

        assert browser.find_element(By.CSS_SELECTOR, locators.main_ingredients)

    @staticmethod
    def test_entrance_from_register(browser):
        browser.get(Url().get_url('register'))

        email, password = User().get_credentials().values()

        # Клик по кнопке "Войти"
        browser.find_element(By.CSS_SELECTOR, locators.link_account).click()

        # Ожидание показа формы входа
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.form_login)))

        # Ввод "Email"
        browser.find_element(By.CSS_SELECTOR, locators.form_login + ' ' + locators.field_name).send_keys(email)

        # Ввод "Пароль"
        browser.find_element(By.CSS_SELECTOR, locators.form_login + ' ' + locators.field_password).send_keys(password)

        # Клик по кнопке "Войти"
        browser.find_element(By.XPATH, locators.button_enter).click()

        # Ожидание открытия главного экрана
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main_ingredients)))

        assert browser.find_element(By.CSS_SELECTOR, locators.main_ingredients)
