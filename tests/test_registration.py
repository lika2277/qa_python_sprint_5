from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from generator import Generator

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Переход на страницу авторизации
# Клик по кнопке "Личный кабинет"
driver.find_element(By.XPATH, ".//a[@href='/account']").click()

# Ожидание показа формы входа
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[@href='/register']")))

# Переход на форму регистрации
# Клик по кнопке "Зарегистрироваться"
driver.find_element(By.XPATH, ".//a[@href='/register']").click()

# Ожидание показа формы регистрации
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Зарегистрироваться']")))

# Ввод данных дял регистрации
# Ввод "Имя"
driver.find_element(By.XPATH, ".//fieldset[1]//input[@type='text']").send_keys("Лика")

# Ввод "Email"
email = Generator.generate_login("liliana_bubnova_19") + '@yandex.ru'
driver.find_element(By.XPATH, ".//fieldset[2]//input[@type='text']").send_keys(email)

# Ввод "Пароль"
password = Generator.generate_password()
driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)

# Клик по кнопке "Зарегистироваться"
driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

# Ожидание показа формы входа
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))

# Ввод "Email"
driver.find_element(By.XPATH, ".//fieldset[1]//input[@type='text']").send_keys(email)

# Ввод "Пароль"
driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)

# Клик по кнопке "Войти"
driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

# Ожидание открытия главного экрана
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[@href='/account']")))

# Переход в личный кабинет
driver.find_element(By.XPATH, ".//a[@href='/account']").click()

# Ожидание открытия личного кабинета
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//main//ul/li[2]//input[@type='text']")))

# Получить значение логина
login = driver.find_element(By.XPATH, "//main//ul/li[2]//input[@type='text']").get_attribute('value')

assert login == email

driver.quit()