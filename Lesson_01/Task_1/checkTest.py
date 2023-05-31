from zeep import Client, Settings
import yaml

with open('addr.yaml') as f:
    wsdl = yaml.safe_load(f)['wsdl']

settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings=settings)


def checkText(word):
    return client.service.checkText(word)[0]['s']
    