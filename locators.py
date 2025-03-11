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
    'constructor': 'a[class^="AppHeader_header__link"][href="/"]',
    'logo': 'div[class^="AppHeader_header__logo"] > a',
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
    'register': './/button[text()="Зарегистрироваться"]',
    'enter_account': 'div[class^="BurgerConstructor_basket__container"] > button'
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

page = {
    'account': 'div[class^="Account_account"]'
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