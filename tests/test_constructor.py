import pytest
import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Url, Constructor

@pytest.fixture(scope = 'function')
def page(browser):
    browser.get(Url().get_url())

    return Constructor(
        browser.find_elements(By.CSS_SELECTOR, locators.constructor.get('tab')),
        browser.find_elements(By.CSS_SELECTOR, locators.constructor.get('heading'))
    )

def test_constructor_switch_bread(browser, page):
    # Заголовок "Булки"
    heading = page.get_heading('Булки')

    # Расчет позиции первой категории
    y = int(heading.rect.get('y'))

    # Отступ у заголовка
    margin = int(heading.value_of_css_property('margin-top')[0:-2])

    # Нажатие на кнопку "Соусы"
    tab = page.get_tab('Соусы')
    tab.click()

    # Ожидание анимации
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of(tab))

    # Нажатие на кнопку "Булки"
    tab = page.get_tab('Булки')
    tab.click()

    # Ожидание анимации
    WebDriverWait(browser, 5, 5).until(expected_conditions.visibility_of(tab))

    assert heading and int(heading.rect.get('y')) <= (y + margin)

def test_constructor_switch_filling(browser, page):
    # Заголовок "Начинки"
    heading = page.get_heading('Начинки')

    # Расчет позиции первой категории
    y = int(heading.rect.get('y'))

    # Нажатие на кнопку "Начинки"
    tab = page.get_tab('Начинки')
    tab.click()

    # Ожидание анимации
    WebDriverWait(browser, 5, 5).until(expected_conditions.visibility_of(tab))

    # Проверка прокрутки до начала области просмотра
    assert int(heading.rect.get('y')) <= y

def test_constructor_switch_souse(browser, page):
    # Заголовок "Начинки"
    heading = page.get_heading('Соусы')

    # Расчет позиции первой категории
    y = int(heading.rect.get('y'))

    # Нажатие на кнопку "Соусы"
    tab = page.get_tab('Соусы')
    tab.click()

    # Ожидание анимации
    WebDriverWait(browser, 5, 5).until(expected_conditions.visibility_of(tab))

    # Проверка прокрутки до начала области просмотра
    assert int(heading.rect.get('y')) <= y