from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import Url

url = Url()

driver = webdriver.Chrome()
driver.get(url.get_url())

# Расчет позиции первой категории (так как она первая по-умолчанию)
y = int(driver.find_element(By.XPATH, './/h2[text()="Булки"]').rect.get('y'))

 # Нажатие на кнопку "Начинки"
driver.find_element(By.XPATH, './/main/section[1]/div/div[3]').click()

# Ожидание анимации
sleep(1)

# Проверка прокрутки до начала области просмотра
assert int(driver.find_element(By.XPATH, './/h2[text()="Начинки"]').rect.get('y')) <= y

driver.quit()