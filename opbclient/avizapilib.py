import ssl
import requests
from requests.auth import HTTPBasicAuth


class GetInterfaceSum(object):
    def __init__(self, host, transport, port, user, password, **kwargs):
        self.url = None

        self.host = host
        self.transport = transport
        self.port = port
        self.user = user
        self.password = password


    def ethernet(self,ano,add):
        '''
        ethernet() supports any user specification input in CLI

        '''
        
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/info/' + ano + '/' + add
        response = requests.get(self.url, auth=HTTPBasicAuth(self.user, self.password), verify=False)
        print(response.content)

    def response(self, ano):
        '''
        response() supports general REST requests

        '''

        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/info/' + ano
        response = requests.get(self.url, auth=HTTPBasicAuth(self.user, self.password), verify=False)
        print(response.content)

    def rules(self, ano, add):
        
        if len(ano) > 1:
            ano1 = ano[0]
            ano2 = ano[1]
        else:
            print("Invalid")

        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/info/' + ano1 + '/' + add + '/' + ano2
        response = requests.get(self.url, auth=HTTPBasicAuth(self.user, self.password), verify=False)
        print(response.content)
