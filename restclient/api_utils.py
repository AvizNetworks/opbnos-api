import ssl
import requests
from requests.auth import HTTPBasicAuth


class GetAPI(object):
    def __init__(self, host, transport, port, user, password, **kwargs):
        self.url = None

        self.host = host
        self.transport = transport
        self.port = port
        self.user = user
        self.password = password


    def response(self, ano):
        '''
        response() supports general REST requests

        '''

        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/info/' + ano
        response = requests.get(self.url, auth=HTTPBasicAuth(self.user, self.password), verify=False)
        print("{}".format(response.content))

    def resp_arg1(self,ano,add):
        '''
        resp_arg1 supports any user specification input in CLI

        '''
        
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/info/' + ano + '/' + add
        response = requests.get(self.url, auth=HTTPBasicAuth(self.user, self.password), verify=False)
        print("{}".format(response.content))

    def resp_arg2(self, ano, add):
        ''' resp_arg2 supports any user specification (i.e. flow name) as well as two attributes'''
        if len(ano) > 1:
            ano1 = ano[0]
            ano2 = ano[1]
        else:
            raise AttributeError('Invalid inputs')

        response = requests.get(self.url, auth=HTTPBasicAuth(self.user, self.password), verify=False)
        print("{}".format(response.content))
