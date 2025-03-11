

# Локаторы для страницы входа
entrance = {
    # Поля ввода
    'inputs': {
        # "Email"
        'email': './/fieldset[1]//input[@type="text"]',
        # "Пароль"
        'password': './/input[@type="password"]'
    }

}
# Главная страница
main = {
    # Кнопки
    'buttons': {
        # Оформить заказ
        'order': './/main/section[2]//button',
        # "Войти"
        'enter': './/main/section[2]//button'
    }
}

# Ссылки
links = {
    # "Войти"
    'login': './/a[@href="/login"]',
    # "Личный кабинет"
    'account': './/a[@href="/account"]',
    # Регистрация
    'register': './/a[@href="/register"]'
}

# Личный кабинет
account = {
    # Поле "Email"
    'email': '//main//ul/li[2]//input[@type="text"]'
}

buttons = {
    # "Войти"
    'enter': './/button[text()="Войти"]',
    'exit': './/button[text()="Выход"]',
    'register': './/button[text()="Зарегистрироваться"]'
}

fields = {
    'registration': {
        'email': './/fieldset[2]//input[@type="text"]',
        'name': './/fieldset[1]//input[@type="text"]'
    }
}

# Локаторы для страницы конструктора
constructor = {
    # Таб переключения секции конструктора
    'tab': 'div[class^="tab_tab__"]',
    # Секции конструктора
    'heading': 'div[class^="BurgerIngredients_ingredients__menuContainer"] > h2'
}