from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import User, Url
from locators import entrance, main, links, buttons

user = User()
url = Url()

email, password = user.get_credentials().values()

driver = webdriver.Chrome()
driver.get(url.get_url())

# Переход в личный кабинет
# Клик по кнопке "Личный кабинет"
driver.find_element(By.XPATH, links.get('account')).click()

# Ожидание показа формы входа
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, buttons.get('enter'))))

# Ввод "Email"
driver.find_element(By.XPATH, entrance.get('inputs').get('email')).send_keys(email)

# Ввод "Пароль"
driver.find_element(By.XPATH, entrance.get('inputs').get('password')).send_keys(password)

# Клик по кнопке "Войти"
driver.find_element(By.XPATH, buttons.get('enter')).click()

# Ожидание открытия главного экрана
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, main.get('buttons').get('order'))))

assert driver.find_element(By.XPATH, main.get('buttons').get('order')).text == 'Оформить заказ'

driver.quit()
