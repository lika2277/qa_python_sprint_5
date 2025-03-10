from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import User

user = User()
email, password = user.get_credentials().values()

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Клик по кнопке "Личный кабинет"
driver.find_element(By.XPATH, ".//a[@href='/account']").click()

# Ожидание показа формы входа
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//form/button[text()='Войти']")))

# Ввод "Email"
driver.find_element(By.XPATH, ".//fieldset[1]//input[@type='text']").send_keys(email)

# Ввод "Пароль"
driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)

# Клик по кнопке "Войти"
driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

# Ожидание открытия главного экрана
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[@href='/account']")))

# Клик по кнопке "Личный кабинет"
driver.find_element(By.XPATH, ".//a[@href='/account']").click()

# Ожидание открытия личного кабинета
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//main//ul/li[2]//input[@type='text']")))

driver.find_element(By.XPATH, '//nav/ul/li/a[@href="/"]').click()

# Ожидание открытия главного экрана
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//main/section[2]//button")))

assert driver.find_element(By.XPATH, ".//main/section[2]//button").text == 'Оформить заказ'

driver.quit()
