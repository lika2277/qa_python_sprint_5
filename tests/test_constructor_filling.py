from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import Url
from locators import constructor

url = Url()

driver = webdriver.Chrome()
driver.get(url.get_url())

# Расчет позиции первой категории (так как она первая по-умолчанию)
y = int(driver.find_element(By.XPATH, constructor.get('sections').get('bread')).rect.get('y'))

 # Нажатие на кнопку "Начинки"
driver.find_element(By.XPATH, constructor.get('tabs').get('filling')).click()

# Ожидание анимации
sleep(1)

# Проверка прокрутки до начала области просмотра
assert int(driver.find_element(By.XPATH, constructor.get('sections').get('filling')).rect.get('y')) <= y

driver.quit()