import ssl
import sys
import csv
import inspect
import requests
from requests.auth import HTTPBasicAuth

#from http.client import HTTPSConnectionvi 

from configparser import ConfigParser as SafeConfigParser
from configparser import Error as SafeConfigParserError

from avizapilib import GetInterfaceSum

config_path = {'~/.nodeinfo.conf'}

DEF_PORT = '8091'
DEF_TRANSPORT = 'https'
DEF_HOST = '10.4.4.56'

class Config(SafeConfigParser):
    '''
    Config class used configparser library function in order to read and parse config file information

    *can add settings to add more device options to config file
    '''
    def __init__(self, filename=None):
        SafeConfigParser.__init__(self)

        self.filename = filename

    def read(self, filename):
        SafeConfigParser.read(self, filename)

    def get_connection(self, name):
        name = 'connection:{}'.format(name)
        if not self.has_section(name):
            return None
        return dict(self.items(name))

    def load(self, filename):
        self.filename = filename
        return self.read(self.filename)



config = Config()

def config_for(name):
    '''returns connection properties based on user input connection name found in .conf file'''
    return config.get_connection(name)

def load_config(name):
    ''' instance of Config utilized to 'load' the configuration file '''
    return config.load(name)

class Connect(object):
    '''
    Connect object utilized to facilitate get request
    '''
    def __init__(self, transport, host,
                    user, password, port, **kwargs):

        self.host = host
        self.transport = transport
        self.port = port
        self.user = user
        self.password = password

        self.url = None

        self.ether = None
        self.cmds = list()
        self.func = list()
        self.key = list()

        with open('a_getcmd.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, line in enumerate(reader):
                if(i==0): self.cmds = line
                if(i==1): self.func = line
                if(i==2): self.key = line

    def str_to_class(str):
        return getattr(sys.modules[__name__], str)

    def execute(self, commands):
        '''
        analyzes CLI and chooses appropriate REST call

        '''

        for i in commands:
            com_spl = i.split()
            uni_com = com_spl[1:]
            if com_spl[0] == 'show':
                Connect.get_execute(self, com_spl, uni_com)


    def get_execute(self, com_spl, uni_com):
        '''
        'show' commands formatting and input validating

        '''
        for_var = list()
        in_cmd = list()
        if len(com_spl) > 2:
            final = " ".join(uni_com)
            for_var.append(final)
            for j in final:
                if '<' in final:
                    ind1 = final.find('<')
                    final = final[:ind1+1]

            in_cmd.append(final)
        elif len(com_spl) == 2:
            final = com_spl[1]
            for_var.append(final)
            in_cmd.append(final)
        else:
            print("Input Error : Invalid CLI input")

        Connect.api_calls(self, in_cmd, for_var)

    def config_execute(self, commands):
        pass

    def api_calls(self, in_cmd, for_var):
        '''
        formatting and direction to appropriate values in .csv file and request function in avizapilib.py
        '''
        show_command = []
        add = None
        for x in range(len(in_cmd)):
            for i in in_cmd:
                if i in self.cmds:
                    idx = self.cmds.index(i)
                    cm_ind = in_cmd.index(i)
                    inp = for_var[cm_ind]
                    i1 = inp.find('<')
                    if i1 > 0:
                        i2 = inp.find('>')
                        add = inp[i1+1:i2]
                        klass = self.func[idx]
                        show_command.append(klass)
                    else:
                        klass = self.func[idx]
                        show_command.append(klass)
                else:
                    print("Invalid command")
        for api in show_command:
            d = GetInterfaceSum(host=self.host, transport=self.transport, port=self.port, user=self.user,
                    password=self.password)
            ano = self.key[idx]

            if add:
                x = getattr(GetInterfaceSum, api)
                #ano = self.key[idx]
                if len(ano) > 2:
                    l_key = ano.split()
                    if "rules" in l_key:
                        ano = l_key
                    else:
                        ano = "/".join(l_key)
                    x(d, ano, add)
                else:
                    x(d, ano, add)
            else:
                x = getattr(GetInterfaceSum, api)
                #ano = self.key[idx]
                if len(ano) > 2:
                    l_key = ano.split()
                    ano = "/".join(l_key)
                    x(d, ano)
                else:
                    x(d, ano)


    def configFlowRules(self, flow=None):
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows/' + flow + '/rules'
        Connect.request(self)
    def configOverride(self,flow=None,r_id=None):
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows/' + flow + '/rules' + r_id +'/override'
        Connect.request(self)
    def configDelete(self,flow=None):
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows/' + flow
        Connect.request(self)
    def configPortChannel(self,pch_id=None):
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/portchannel/' + pch_id
        Connect.request(self)
    def configInterface(self,intf_name=None):
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/interfaces/config/' + intf_name
        Connect.request(self)
    def configInterfaceNPB(self,intf_name=None):
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/opbinterfaces/' + intf_name
        Connect.request(self)
    def configClearFlowCount(self,flow=None,r_id=None):
        ##clear flow counters
        if flow != None:
            self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/stats/clear/flows/' + flow
        elif flow != None and r_id != None:
            self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/stats/clear/flows/' + flow + '/rules/' + r_id
        else:
            self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/stats/clear/all'
        Connect.request(self)
    def configClearCountAll(self):
        #clear flow counters all
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/stats/clear'
        Connect.request(self)
    def configReboot(self):
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/reboot'
        Connect.request(self)
    def configZTP(self):
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/ztp'
        Connect.request(self)
    def configZTP(self):
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/ztp'
        Connect.request(self)

    def request(self):
        response = requests.get(self.url, auth=HTTPBasicAuth(self.user, self.password), verify=False)
        print(response.content)


def connect(host=None, transport=None, user='admin',
            password='admin', port=None, return_node=True,**kwargs):
    ''':
        creates connection via Connect class; input indicates the connection setting (Default values available for
        port, transport and host)
    '''

    port = port or DEF_PORT
    transport = transport or DEF_TRANSPORT
    host = host or DEF_HOST

    if return_node:
        return Connect(transport=transport, host=host,
                    user=user, password=password, port=port, **kwargs)

def connect_to(name):
    '''
        finds connection specififcations via inputted config file name
    '''
    kwargs = config_for(name)

    if not kwargs:
        raise AttributeError('connection profile not found in config')

    node = connect(return_node=True, **kwargs)
    return node





