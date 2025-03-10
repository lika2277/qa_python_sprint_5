class User:
    def __init__(self):
        self.credentials = [
            {
                'email': 'liliana_bubnova_19_986@yandex.ru',
                'password': '682502'
            }
        ]

    def get_credentials(self):
        return self.credentials[0]

class Url:
    def __init__(self, domain = 'https://stellarburgers.nomoreparties.site'):
        self.domain = domain
        self.path = {
            'main': '/',
            'account': '/account',
            'register': '/register',
            'forgot': '/forgot-password'
        }

    def get_url(self, key = 'main'):
        return  self.domain + self.path[key]