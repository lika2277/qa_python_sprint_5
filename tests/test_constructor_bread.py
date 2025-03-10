from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Отступ у заголовка
diff = 40

# Расчет позиции первой категории (так как она первая по-умолчанию)
y = int(driver.find_element(By.XPATH, './/h2[text()="Булки"]').rect.get('y'))

# Нажатие на кнопку "Соусы"
driver.find_element(By.XPATH, './/main/section[1]/div/div[2]').click()

# Нажатие на кнопку "Булки"
driver.find_element(By.XPATH, './/main/section[1]/div/div[1]').click()

# Ожидание анимации
sleep(1)

# Проверка прокрутки до начала области просмотра
assert int(driver.find_element(By.XPATH, './/h2[text()="Булки"]').rect.get('y')) <= (y + diff)

driver.quit()