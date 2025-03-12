from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructor:

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def test_constructor_switch_sause(browser, page):
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