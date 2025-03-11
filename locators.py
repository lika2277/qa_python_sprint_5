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

# Ссылки
links = {
    # "Войти"
    'login': './/a[@href="/login"]',
    # "Личный кабинет"
    'account': 'a[class^="AppHeader_header__link"][href="/account"]',
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
    },
    'email': 'fieldset[class^="Auth_fieldset"] input[type="text"][name="name"]',
    'password': 'fieldset[class^="Auth_fieldset"] input[type="password"]'
}

forms = {
    'login': 'form[class^="Auth_form__"]'
}

# Локаторы для страницы конструктора
constructor = {
    # Таб переключения секции конструктора
    'tab': 'div[class^="tab_tab__"]',
    # Секции конструктора
    'heading': 'div[class^="BurgerIngredients_ingredients__menuContainer"] > h2'
}

# Главная страница
main = {
    'ingredients': 'section[class^="BurgerIngredients_ingredients"]',
    # Кнопки
    'buttons': {
        # Оформить заказ
        'order': './/main/section[2]//button',
        # "Войти"
        'enter': './/main/section[2]//button'
    }
}