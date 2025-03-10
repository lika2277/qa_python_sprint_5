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
password = Generator.generate_password(0,99999)
driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)

# Клик по кнопке "Зарегистироваться"
driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

# Красная рамка вокруг поля "Пароль"
error_input = driver.find_element(By.CSS_SELECTOR, ".input.input_type_password.input_size_default.input_status_error")

# Сообщение об ошибке
error_message = driver.find_element(By.CSS_SELECTOR, ".input__error.text_type_main-default")

assert error_message and error_input

driver.quit()