import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import User, Url

def test_entrance_from_cabinet(browser):
    browser.get(Url().get_url())

    email, password = User().get_credentials().values()

    # Клик по кнопке "Личный кабинет"
    browser.find_element(By.CSS_SELECTOR, locators.links.get('account')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.forms.get('login'))))

    # Ввод "Email"
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('email')).send_keys(email)

    # Ввод "Пароль"
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('password')).send_keys(password)

    # Клик по кнопке "Войти"
    browser.find_element(By.XPATH, locators.buttons.get('enter')).click()

    # Ожидание открытия главного экрана
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main.get('ingredients'))))

    assert browser.find_element(By.CSS_SELECTOR, locators.main.get('ingredients'))

def test_entrance_from_forgot_password(browser):
    browser.get(Url().get_url('forgot'))

    email, password = User().get_credentials().values()

    # Клик по кнопке "Войти"
    browser.find_element(By.CSS_SELECTOR, locators.links.get('account')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.forms.get('login'))))

    # Ввод "Email"
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('email')).send_keys(email)

    # Ввод "Пароль"
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('password')).send_keys(password)

    # Клик по кнопке "Войти"
    browser.find_element(By.XPATH, locators.buttons.get('enter')).click()

    # Ожидание открытия главного экрана
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main.get('ingredients'))))

    assert browser.find_element(By.CSS_SELECTOR, locators.main.get('ingredients'))

def test_entrance_from_main(browser):
    browser.get(Url().get_url())

    email, password = User().get_credentials().values()

    # Клик по кнопке "Войти"
    browser.find_element(By.CSS_SELECTOR, locators.links.get('account')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.forms.get('login'))))

    # Ввод "Email"
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('email')).send_keys(email)

    # Ввод "Пароль"
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('password')).send_keys(password)

    # Клик по кнопке "Войти"
    browser.find_element(By.XPATH, locators.buttons.get('enter')).click()

    # Ожидание открытия главного экрана
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main.get('ingredients'))))

    assert browser.find_element(By.CSS_SELECTOR, locators.main.get('ingredients'))

def test_entrance_from_register(browser):
    browser.get(Url().get_url('register'))

    email, password = User().get_credentials().values()

    # Клик по кнопке "Войти"
    browser.find_element(By.CSS_SELECTOR, locators.links.get('account')).click()

    # Ожидание показа формы входа
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.forms.get('login'))))

    # Ввод "Email"
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('email')).send_keys(email)

    # Ввод "Пароль"
    browser.find_element(By.CSS_SELECTOR, locators.forms.get('login') + ' ' + locators.fields.get('password')).send_keys(password)

    # Клик по кнопке "Войти"
    browser.find_element(By.XPATH, locators.buttons.get('enter')).click()

    # Ожидание открытия главного экрана
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locators.main.get('ingredients'))))

    assert browser.find_element(By.CSS_SELECTOR, locators.main.get('ingredients'))
