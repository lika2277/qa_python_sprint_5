from selenium.webdriver.remote.webelement import WebElement

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

class Constructor:
    def __init__(self, tabs: list[WebElement], headings: list[WebElement]):
        self.tabs = tabs
        self.headings = headings

    def get_tab(self, value = ''):
        if not property or not value:
            return None

        for tab in self.tabs:
            if tab.get_property('innerText') == value:
                return tab

    def get_heading(self, value= ''):
        if not property or not value:
            return None

        for heading in self.headings:
            if heading.get_property('innerText') == value:
                return heading