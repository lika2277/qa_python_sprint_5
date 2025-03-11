import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import User, Url

def test_personal_account_enter(browser):
    browser.get(Url().get_url())

    email, password = User().get_credentials().values()

    # Клик по кнопке "Войти"
    browser.find_element(By.CSS_SELECTOR, locators.buttons.get('enter_account')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.forms.get('login'))))

    # Ввод "Email"
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('name')).send_keys(email)

    # Ввод "Пароль"
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('password')).send_keys(password)

    # Клик по кнопке "Войти"
    browser.find_element(By.XPATH, locators.buttons.get('enter')).click()

    # Ожидание открытия главного экрана
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main.get('ingredients'))))

    # Клик по кнопке "Войти"
    browser.find_element(By.CSS_SELECTOR, locators.links.get('account')).click()

    # Ожидание открытия личного кабинета
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.page.get('account'))))

    assert browser.find_element(By.CSS_SELECTOR, locators.page.get('account'))

def test_personal_account_exit(browser):
    browser.get(Url().get_url())

    email, password = User().get_credentials().values()

    # Клик по кнопке "Личный кабинет"
    browser.find_element(By.CSS_SELECTOR, locators.links.get('account')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.forms.get('login'))))

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

    # Клик по кнопке "Выйти"
    browser.find_element(By.XPATH, locators.buttons.get('exit')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.forms.get('login'))))

    assert browser.find_element(By.CSS_SELECTOR, locators.forms.get('login'))

def test_personal_account_to_constructor(browser):
    browser.get(Url().get_url())

    email, password = User().get_credentials().values()

    # Клик по кнопке "Войти"
    browser.find_element(By.CSS_SELECTOR, locators.buttons.get('enter_account')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.forms.get('login'))))

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

    browser.find_element(By.CSS_SELECTOR, locators.links.get('constructor')).click()

    # Ожидание открытия главного экрана
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main.get('ingredients'))))

    assert browser.find_element(By.CSS_SELECTOR, locators.main.get('ingredients'))

def test_personal_account_to_logo(browser):
    browser.get(Url().get_url())

    email, password = User().get_credentials().values()

    # Клик по кнопке "Войти"
    browser.find_element(By.CSS_SELECTOR, locators.buttons.get('enter_account')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.forms.get('login'))))

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

    browser.find_element(By.CSS_SELECTOR, locators.links.get('logo')).click()

    # Ожидание открытия главного экрана
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main.get('ingredients'))))

    assert browser.find_element(By.CSS_SELECTOR, locators.main.get('ingredients'))