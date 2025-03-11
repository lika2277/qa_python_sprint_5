# Ссылки
links = {
    # "Войти"
    'login': './/a[@href="/login"]',
    # "Личный кабинет"
    'account': 'a[class^="AppHeader_header__link"][href="/account"]',
    # Страница конструктора
    'constructor': 'a[class^="AppHeader_header__link"][href="/"]',
    # Логотип
    'logo': 'div[class^="AppHeader_header__logo"] > a',
    # Регистрация
    'register': 'a[class^="Auth_link"][href="/register"]'
}

# Личный кабинет
account = {
    # Поле "Email"
    'email': '//main//ul/li[2]//input[@type="text"]'
}

# Кнопки
buttons = {
    # "Войти"
    'enter': './/button[text()="Войти"]',
    # "ВЫйти"
    'exit': './/button[text()="Выход"]',
    # "Регистрация"
    'register': './/button[text()="Зарегистрироваться"]',
    # "Войти в аккаунт"
    'enter_account': 'div[class^="BurgerConstructor_basket__container"] > button'
}

# Поля
fields = {
    # "Имя"
    'name': 'fieldset[class^="Auth_fieldset_"]:nth-child(1) input[type="text"]',
    # "Email"
    'email': 'fieldset[class^="Auth_fieldset"]:nth-child(2) input[type="text"]',
    # "Пароль"
    'password': 'fieldset[class^="Auth_fieldset"] input[type="password"]'
}

# Ошибки
errors = {
    # Красная рамка фокруг поля "Пароль"
    'field': '.input.input_type_password.input_size_default.input_status_error',
    # Сообщение об ошибке
    'message': '.input__error.text_type_main-default'
}

#  Формы
forms = {
    'login': 'form[class^="Auth_form__"]',
}

# Локаторы для страницы конструктора
constructor = {
    # Таб переключения секции конструктора
    'tab': 'div[class^="tab_tab__"]',
    # Секции конструктора
    'heading': 'div[class^="BurgerIngredients_ingredients__menuContainer"] > h2'
}

# Страницы
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