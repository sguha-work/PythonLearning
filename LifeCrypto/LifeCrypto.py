from datetime import datetime


class LifeCrypto:

    __timeStamp = None
    __inputString = ''

    def __init__(self):
        self.timeStamp = datetime.now()

    def __init__(self, timeStamp):
        self.timeStamp = timeStamp

    def encrypt(self, userGivenString):

        pass
