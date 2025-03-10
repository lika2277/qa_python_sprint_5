from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from generator import Generator
from data import Url
from locators import links, fields, buttons, entrance

url = Url()

driver = webdriver.Chrome()
driver.get(url.get_url())

# Переход на страницу авторизации
# Клик по кнопке "Личный кабинет"
driver.find_element(By.XPATH, links.get('account')).click()

# Ожидание показа формы входа
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, links.get('register'))))

# Переход на форму регистрации
# Клик по кнопке "Зарегистрироваться"
driver.find_element(By.XPATH, links.get('register')).click()

# Ожидание показа формы регистрации
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, buttons.get('register'))))

# Ввод данных дял регистрации
# Ввод "Имя"
driver.find_element(By.XPATH, fields.get('registration').get('name')).send_keys("Лика")

# Ввод "Email"
email = Generator.generate_login("liliana_bubnova_19") + '@yandex.ru'
driver.find_element(By.XPATH, fields.get('registration').get('email')).send_keys(email)

# Ввод "Пароль"
password = Generator.generate_password(0,99999)
driver.find_element(By.XPATH, entrance.get('inputs').get('password')).send_keys(password)

# Клик по кнопке "Зарегистироваться"
driver.find_element(By.XPATH, buttons.get('register')).click()

# Красная рамка вокруг поля "Пароль"
error_input = driver.find_element(By.CSS_SELECTOR, ".input.input_type_password.input_size_default.input_status_error")

# Сообщение об ошибке
error_message = driver.find_element(By.CSS_SELECTOR, ".input__error.text_type_main-default")

assert error_message and error_input

driver.quit()