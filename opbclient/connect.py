import requests
from requests.auth import HTTPBasicAuth

class Connect:

    def __init__(self, host, transport, port='8091',
            user='admin', password='admin', url=None):
        self.ip = host
        self.transport = transport
        self.port = port
        self.user = user
        self.password = password
        self.url = url

    def execute(self, command):

        #for j in len(command):
        for i in command:
            if i  == 'show interfaces':
                url = self.transport + '://' + self.ip + ':' + self.port + '/api/info/interfaces'
                print(url)
                response = requests.get(url, auth = HTTPBasicAuth('admin','admin'),verify=False)
                print(response.content)
            else:
                print("reach")
