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