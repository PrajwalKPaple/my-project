import configparser

from pytest_html.extras import url

config = configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseUrl')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password




