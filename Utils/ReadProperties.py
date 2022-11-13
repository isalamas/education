import configparser

config = configparser.RawConfigParser()
configFilePath = r'C:\Users\LA\PycharmProjects\itworx education\Configurations\config.ini'
config.read(configFilePath)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url