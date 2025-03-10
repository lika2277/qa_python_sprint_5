# Sprint_5: Финальный проект

Часть автотестов использует данные почты и пароля уже авторизованного пользователя, для указания этих данных вам необходимо указать следующие переменные окружения:

```commandline
TEST_EMAIL=<email авторизованного пользователя>
TEST_PASSWORD=<пароль авторизованного пользователя>
```
например, для Powershell:

```commandline
$Env:TEST_EMAIL = "some_email@yandex.ru"
$Env:TEST_PASSWORD = "123456"
```

Запуск автотестов:

```commandline
python <название файла автотеста>
```

например:

```commandline
python .\tests\test_entrance_from_cabinet.py
```