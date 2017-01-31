import random
from datetime import date


class Message(object):
    def __init__(self, client, text, message_type):
        self.client = client
        self.text = text
        self.message_type = message_type
        self.error = None

    def __str__(self):
        return "client: %s, text: %s, type: %s" % (str(self.client), self.text, str(self.message_type))

    @staticmethod
    def message(client):
        text = "".join([random.choice(u'йцукенгшщзхъфывапролджэёячсмитьбю') for _ in range(20)])
        text += str(date.today())
        return Message(client, text, 3)
