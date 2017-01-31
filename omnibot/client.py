import random

MIN = 795812313215
MAX = 795853659998


class Client(object):
    def __init__(self, name, login):
        self.name = name
        self.login = login

    def __str__(self):
        return 'login: %s, name: %s' % (self.login, self.name)

    @staticmethod
    def client(data):
        login = str(data)
        name = str(data)
        return Client(name, login)

    @staticmethod
    def clients(size):
        phones = range(MIN, MAX+1)
        logins = random.sample(phones, min(len(phones), size))
        return list(map(Client.client, logins))
