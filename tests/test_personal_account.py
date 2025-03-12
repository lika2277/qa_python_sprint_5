import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import user, urls

class TestPersonalAccount:

    @staticmethod
    def test_personal_account_enter(browser):
        browser.get(urls.get('main'))

        email, password = user.values()

        # Клик по кнопке "Войти"
        browser.find_element(By.CSS_SELECTOR, locators.button_enter_account).click()

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

        # Клик по кнопке "Войти"
        browser.find_element(By.CSS_SELECTOR, locators.link_account).click()

        # Ожидание открытия личного кабинета
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.page_account)))

        assert browser.find_element(By.CSS_SELECTOR, locators.page_account)

    @staticmethod
    def test_personal_account_exit(browser):
        browser.get(urls.get('main'))

        email, password = user.values()

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

        # Клик по кнопке "Личный кабинет"
        browser.find_element(By.CSS_SELECTOR, locators.link_account).click()

        # Ожидание открытия личного кабинета
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.page_account)))

        # Клик по кнопке "Выйти"
        browser.find_element(By.XPATH, locators.button_exit).click()

        # Ожидание показа формы входа
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.form_login)))

        assert browser.find_element(By.CSS_SELECTOR, locators.form_login)

    @staticmethod
    def test_personal_account_to_constructor(browser):
        browser.get(urls.get('main'))

        email, password = user.values()

        # Клик по кнопке "Войти"
        browser.find_element(By.CSS_SELECTOR, locators.button_enter_account).click()

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

        # Клик по кнопке "Личный кабинет"
        browser.find_element(By.CSS_SELECTOR, locators.link_account).click()

        # Ожидание открытия личного кабинета
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.page_account)))

        browser.find_element(By.CSS_SELECTOR, locators.link_constructor).click()

        # Ожидание открытия главного экрана
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main_ingredients)))

        assert browser.find_element(By.CSS_SELECTOR, locators.main_ingredients)

    @staticmethod
    def test_personal_account_to_logo(browser):
        browser.get(urls.get('main'))

        email, password = user.values()

        # Клик по кнопке "Войти"
        browser.find_element(By.CSS_SELECTOR, locators.button_enter_account).click()

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

        # Клик по кнопке "Личный кабинет"
        browser.find_element(By.CSS_SELECTOR, locators.link_account).click()

        # Ожидание открытия личного кабинета
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.page_account)))

        browser.find_element(By.CSS_SELECTOR, locators.link_logo).click()

        # Ожидание открытия главного экрана
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main_ingredients)))

        assert browser.find_element(By.CSS_SELECTOR, locators.main_ingredients)