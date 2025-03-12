# Ссылки
# "Личный кабинет"
link_account = 'a[class^="AppHeader_header__link"][href="/account"]'
# Страница конструктора
link_constructor = 'a[class^="AppHeader_header__link"][href="/"]'
# Логотип
link_logo = 'div[class^="AppHeader_header__logo"] > a'
# Регистрация
link_register = 'a[class^="Auth_link"][href="/register"]'

# Кнопки
# "Войти"
button_enter = './/button[text()="Войти"]'
# "ВЫйти"
button_exit = './/button[text()="Выход"]'
# "Регистрация"
button_register = './/button[text()="Зарегистрироваться"]'
# "Войти в аккаунт"
button_enter_account = 'div[class^="BurgerConstructor_basket__container"] > button'

# Поля
# "Имя"
field_name = 'fieldset[class^="Auth_fieldset_"]:nth-child(1) input[type="text"]'
# "Email"
field_email = 'fieldset[class^="Auth_fieldset"]:nth-child(2) input[type="text"]'
# "Пароль"
field_password = 'fieldset[class^="Auth_fieldset"] input[type="password"]'

# Ошибки
# Красная рамка фокруг поля "Пароль"
error_field = '.input.input_type_password.input_size_default.input_status_error'
# Сообщение об ошибке
error_message = '.input__error.text_type_main-default'

#  Формы
form_login = 'form[class^="Auth_form__"]'

# Локаторы для страницы конструктора
# Таб переключения секции конструктора
constructor_tab = 'div[class^="tab_tab__"]'
# Секции конструктора
constructor_heading = 'div[class^="BurgerIngredients_ingredients__menuContainer"] > h2'

# Страницы
page_account = 'div[class^="Account_account"]'

# Главная страница
main_ingredients = 'section[class^="BurgerIngredients_ingredients"]'