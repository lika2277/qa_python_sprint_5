import random

class Generator:
    @staticmethod
    def generate_login(prefix):
        return prefix + "_" + str(random.randint(0, 999))

    @staticmethod
    def generate_password(start = 0, stop = 999999):
        return  str(random.randint(start, stop))