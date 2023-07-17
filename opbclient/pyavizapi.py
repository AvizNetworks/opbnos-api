import ssl
import sys
import csv
import inspect
import requests
from requests.auth import HTTPBasicAuth


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
        
        with open('flow_input.json', 'r') as flowjson:
            self.j = json.load(flowjson)

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


    def configFlow(self):
        ''' Config flow basic function '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows'
        dt = self.j["configFlow"] #'configFlow' index in json
        #print(dt)

        headers = {"Content-Type": "application/json"}

        Connect.request(self, dt, headers) #request() -> post request

    def configFlowRules(self, flow=None):
        ''' Config flow rules '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows/flow1/rules'

        for f in self.j["configRules"]:
            if f == flow:
                dt = self.j["configRules"][flow]

        headers = {"Content-Type": "application/json"}

        Connect.request(self, dt, headers)
    def configOverride(self,flow=None,r_id=None):
        ''' Flow override '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows/' + flow + '/rules' + r_id +'/override'
        dt = {"override-to": ["Ethernet6_1", "Ethernet7_1"],
                "override-push-vlan-tag": "100",
                "override-pop-vlan": "disable"
                }
        Connect.request(self, dt)
    def configDelete(self,flow=None):
        ''' Flow delete override '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows/' + flow
        Connect.request(self)

    def configDeleteRules(flow=None, r_id=None):
        ''' Flow delete rule/flow'''
        if r_id == None:
            self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows/' + flow
            Connect.request(self)
        else:
            self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows/' + flow + '/rules' + r_id
            Connect.request(self)
    
    def configPortChannel(self,pch_id=None, port_list=None, dsp=None):
        ''' Config port channel '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/portchannel/' + pch_id
        dt = {"add_member": port_list,
                "description": dsp
                }
        Connect.request(self, dt)
    
    def configInterface(self,intf_name=None):
        ''' Config interface '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/interfaces/config/' + intf_name

        for f in self.j["configInterface"]:
            if f == intf_name:
                dt = self.j["configInterface"][intf_name]

        Connect.request(self, dt)
    
    def configInterfaceNPB(self,intf_name=None,igr-vlan=None, egr-tag=None):
        ''' Config interface NPB '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/opbinterfaces/' + intf_name
        dt = {"name": intf_name,
                "ingress-vlan": igr-vlan,
                "egress-tagging": egr-tag
                }
        Connect.request(self, dt)
    
    def configClearFlowCount(self,flow=None,r_id=None):
        ''' Config clear flow counters/rule '''
        if flow != None:
            self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/stats/clear/flows/' + flow
        elif flow != None and r_id != None:
            self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/stats/clear/flows/' + flow + '/rules/' + r_id
        else:
            self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/stats/clear/all'
        Connect.request(self)
    
    def configClearCountAll(self):
        ''' Config clear counters all '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/stats/clear'
        Connect.request(self)
    
    def configReboot(self):
        ''' Config reboot '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/reboot'
        dt = {"reboot": "yes"}
        Connect.request(self, dt)
    
    def configZTP(self):
        ''' Config ZTP '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/ztp'
        dt = {"ztp_status": "enable | disable"}
        Connect.request(self, dt)
    
    def configSNMP(self):
        ''' Config snmp trap '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/snmptrap'
        dt = {"version": 2,
                "server_id": 6,
                "community": "Aviz1",
                "ip_address": "10.2.2.10"
                }
        Connect.request(self, dt)
    
    def configSNMPcomm(self):
        ''' Config snmp community '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/snmp-community'
        dt = {"community": "Aviz"}
        Connect.request(self, dt)
    
    def configSNMPthreshold(self):
        ''' Config snmp threshold '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/snmp/threshold'
        dt = {"mem_util_threshold": "10",
                "cpu_util_threshold": "30",
                "disk_util_threshold": "40"
        }
        Connect.request(self, dt)
    
    def configSNMPusers(type):
        ''' Config snmp users (Priv type) '''
        #clear flow counters all
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/ntp/128.138.141.172'
        
        for f in self.j["configSNMPusers"]:
            if f == flow:
                dt = self.j["configSNMPusers"][type]        

        Connect.request(self, dt)
    
    def configTACACS(self):
        ''' Config TACACS+ '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/tacacs-server/10.4.4.11'
        dt = {"host": "10.4.4.11",
                "timeout": 8,
                "priority": 1,
                "auth_type": "pap",
                "passkey": "support"
                }
        Connect.request(self, dt)
    
    def configTACACSglobal(self):
        ''' Config TACACS global '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/tacacs-server/global'
        dt = {"auth_type": "pap",
                "timeout": 8,
                "passkey": "support"
                }
        Connect.request(self, dt)
    
    def configNTP(self, ip = None):
        ''' Config ntp '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/ntp/' + ip
        Connect.request(self)
    
    def configTimezone(self):
        ''' Config timezone '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/clock'
        dt = {"timezone": "Asia/Kolkata"}
        Connect.request(self, dt)
    
    def configFFPsupport(self):
        ''' Config Finisar SFP support '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/tx-enable'
        Connect.request(self)


    def request(self, dt=None):
        ''' Creates post request'''

        headers = {"Content-Type": "application/json"}

        if dt == None:
            response = requests.post(self.url, auth=HTTPBasicAuth(self.user, self.password), headers=headers, verify=False)
            print(response.status_code()) #shows port request success/fail
        else:
            data = json.dumps(dt) #access to json file data
            response = requests.post(self.url, auth=HTTPBasicAuth(self.user, self.password), headers=headers, data=data, verify=False)
            print(response.status_code())

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





