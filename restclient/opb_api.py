import ssl
import sys
import csv
import json
import inspect
import requests
from requests.auth import HTTPBasicAuth


from configparser import ConfigParser as SafeConfigParser
from configparser import Error as SafeConfigParserError

from api_utils import GetAPI

config_path = {'~/.nodeinfo.conf'}

DEF_PORT = '443'
DEF_TRANSPORT = 'https'
DEF_HOST = '10.4.4.56'
DEF_NODEFILE = 'nodeinfo.conf'


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

    def get_device(self, name):
        name = 'Device:{}'.format(name)
        if not self.has_section(name):
            return None
        return dict(self.items(name))

    def load(self, filename):
        self.filename = filename
        return self.read(self.filename)


config = Config()

def config_for(name):
    '''returns connection properties based on user input connection name found in .conf file'''
    return config.get_device(name)

class Connect(object):
    '''
    Connect object utilized to facilitate the OPB device
    '''
    def __init__(self, transport, host,
                    user, password, port, name, **kwargs):

        self.host = host
        self.transport = transport
        self.port = port
        self.user = user
        self.password = password
        self.name = name + '.json'

        self.url = None

        self.cmds = list()
        self.func = list()
        self.key = list()

        with open('getcmd.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                self.cmds.append(line[0])
                self.func.append(line[1])
                self.key.append(line[2])

        with open(self.name, 'r') as flowjson:
            self.device_conf = json.load(flowjson)

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
            d = GetAPI(host=self.host, transport=self.transport, port=self.port, user=self.user,
                    password=self.password)
            ano = self.key[idx]

            if add:
                x = getattr(GetAPI, api)
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
                x = getattr(GetAPI, api)
                #ano = self.key[idx]
                if len(ano) > 2:
                    l_key = ano.split()
                    ano = "/".join(l_key)
                    x(d, ano)
                else:
                    x(d, ano)


    def configFlow(self, flow):
        ''' Config flow basic function 
            
            -> accesses user input flow and function specified indexes to obtain request body

        '''

        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows'
        for f in self.device_conf:
            if f == flow:
                dt = self.device_conf[flow]["configFlow"] #'configFlow' index in json

        Connect.request(self, dt) #request() -> post request

    def configFlowAllRules(self, flow):
        ''' Config all flow rules '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows/' + flow + '/rules'
        Connect.request(self)
        
    def configFlowRules(self, flow, r_id):
        ''' Config flow rules '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows/' + flow + '/rules'
        for f in self.device_conf:
            if f == flow:
                dt = self.device_conf[flow]['configRules'][r_id]

        Connect.request(self, dt)
        
    def deleteAndConfigFlowRule(self, flow, r_id):
        ''' Delete flows and config flow/rules '''

        headers = {"Content-Type": "application/json"}
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows/' + flow + '/rules' + r_id
        response = requests.delete(self.url, auth=HTTPBasicAuth(self.user, self.password), headers=headers, verify=False)
        print(response.status_code)

        Connect.configFlowRules(self,flow,r_id)
        
    def configOverride(self, flow, r_id, dt):
        ''' Flow override flow/rule'''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows/' + flow + '/rules' + r_id +'/override'
        Connect.request(self, dt)

    def configDelete(self,flow):
        ''' Flow delete flow '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows/' + flow
        Connect.delete(self)

    def configDeleteRules(self, flow, r_id):
        ''' Flow delete rule'''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/flows/' + flow + '/rules' + r_id
        
        Connect.delete(self)

    def configPortChannel(self, pch_id, port_list, dsp=None):
        ''' Config port channel '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/portchannel/' + pch_id
        #Example:
        ##dt = {"add_member": port_list,
        ##        "description": dsp
        ##        }
        dt = dict()

        if port_list != None:
            dt["add_member"] = port_list
        if dsp != None:
            dt["description"] = dsp
        else:
            pass

        Connect.request(self, dt)

    def configInterface(self,intf_name):
        ''' Config interface '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/interfaces/config/' + intf_name

        for f in self.device_conf:
            if f == "configInterface":
                dt = self.device_conf["configInterface"][intf_name]

        Connect.request(self, dt)

    def configAllInterfaces(self):
        ''''''
        intf_names = list()
        for f in self.device_conf["configInterface"]:
            intf_names.append(f)
            
            for name in intf_names:
                self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/interfaces/config/' + name
                dt = self.device_conf["configInterface"][name]
                Connect.request(self, dt)

    def configInterfaceNPB(self, intf_name=None,igr_vlan=None, egr_tag=None):
        ''' Config interface NPB '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/opbinterfaces/' + intf_name
        #Example:
        ##dt = {"name": intf_name,
        ##        "ingress-vlan": igr-vlan,
        ##        "egress-tagging": egr-tag
        ##        }
        dt = dict()

        if intf_name != None:
            dt["intf_name"] = intf_name
        if igr_vlan != None:
            dt["ingress-vlan"] = igr_vlan
        if egr_tag != None:
            dt["egr_tag"] = egr_tag
        else:
            pass
        
        Connect.request(self, dt)

    def clearFlowCounters(self,flow=None,r_id=None):
        ''' Clear flow counters/rule '''
        if flow != None:
            self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/stats/clear/flows/' + flow
        elif flow != None and r_id != None:
            self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/stats/clear/flows/' + flow + '/rules/' + r_id
        else:
            self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/stats/clear/all'
        Connect.request(self)

    def clearInterfaceCounters(self):
        ''' Clear interface counters '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/interfaces/config/stats/clear'
        Connect.request(self)

    def configReboot(self, dt):
        ''' Config reboot '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/reboot'

        #Example: dt = {"reboot": "yes"}

        Connect.request(self, dt)

    def configZTP(self, dt):
        ''' Config ZTP '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/ztp'

        #Example: dt = {"ztp_status": "enable | disable"}

        Connect.request(self, dt)

    def configSNMP(self, dt):
        ''' Config snmp trap '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/snmptrap'

        #Example: 
        ##dt = {"version": 2,
        ##        "server_id": 6,
        ##        "community": "Aviz1",
        ##        "ip_address": "10.2.2.10"
        ##        }

        Connect.request(self, dt)

    def configSNMPcomm(self, dt):
        ''' Config snmp community '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/snmp-community'

        #Example: dt = {"community": "Aviz"}

        Connect.request(self, dt)

    def configSNMPthreshold(self, dt):
        ''' Config snmp threshold '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/snmp/threshold'

        #Example:
        ##dt = {"mem_util_threshold": "10",
        ##        "cpu_util_threshold": "30",
        ##        "disk_util_threshold": "40"
        ##}

        Connect.request(self, dt)

    def configSNMPusers(self, dt):
        ''' Config snmp users (Priv type) '''
        #clear flow counters all
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/ntp/128.138.141.172'

        #Example:
                #"Priv": {
                #        "username": "testuser6",
                #        "priv_type": "Priv",
                #        "auth": "MD5",
                #        "auth_pwd": "testuser4_auth_pass",
                #        "enc": "AES",
                #        "enc_pwd": "testuser3_encrypt_pass",
                #        "access": "RO"
                #},

                #"AuthNoPriv": {
                #        "username": "testuser3",
                #        "priv_type": "AuthNoPriv",
                #        "auth": "MD5",
                #        "auth_pwd": "testuser3_auth_pass",
                #        "access": "RO"
                #},

                #"NoAuthNoPriv": {
                #        "username": "user35",
                #        "priv_type": "noAuthNoPriv",
                #        "access": "RO"
                #}

        Connect.request(self, dt)

    def configTACACS(self, dt):
        ''' Config TACACS+ '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/tacacs-server/10.4.4.11'

        #Example:
        ##dt = {"host": "10.4.4.11",
        ##        "timeout": 8,
        ##        "priority": 1,
        ##        "auth_type": "pap",
        ##        "passkey": "support"
        ##        }

        Connect.request(self, dt)

    def configTACACSglobal(self, dt):
        ''' Config TACACS global '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/tacacs-server/global'

        #Example:
        ##dt = {"auth_type": "pap",
        ##        "timeout": 8,
        ##        "passkey": "support"
        ##        }

        Connect.request(self, dt)

    def configNTP(self, ip):
        ''' Config ntp '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/ntp/' + ip
        Connect.request(self)

    def configTimezone(self, dt):
        ''' Config timezone '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/clock'

        #Example: dt = {"timezone": "Asia/Kolkata"}

        Connect.request(self, dt)

    def configTXEnable(self):
        ''' Config Finisar SFP support '''
        self.url = self.transport + '://' + self.host + ':' + self.port + '/api/config/tx-enable'
        Connect.request(self)


    def request(self, dt=None):
        ''' Creates post request'''

        headers = {"Content-Type": "application/json"}

        if dt == None:
            response = requests.post(self.url, auth=HTTPBasicAuth(self.user, self.password), headers=headers, verify=False)
            print(response.status_code()) #shows post request success/fail
        else:
            data = json.dumps(dt) #access to json file data
            response = requests.post(self.url, auth=HTTPBasicAuth(self.user, self.password), headers=headers, data=data, verify=False)
            #print(response.status_code)
            print("Status : {} -> Response : {}".format(response.status_code, response.content)) #shows delete request success/fail
            #print(response.())

    def delete(self):
        
        headers = {"Content-Type": "application/json"}

        response = requests.delete(self.url, auth=HTTPBasicAuth(self.user, self.password), headers=headers, verify=False)
        print("Status : {} -> Response : {}".format(response.status_code, response.content)) #shows delete request success/fail

def connect(host, name, transport=None, user='admin',
            password='admin', port=None, return_node=True,**kwargs):
    ''':
        creates connection via Connect class; input indicates the connection setting (Default values available for
        port, transport and host)
    '''

    port = port or DEF_PORT
    transport = transport or DEF_TRANSPORT
    #host = host or DEF_HOST
    if host == None:
        raise AttributeError('Invalid request; please enter host ip')

    if return_node:
        return Connect(transport=transport, host=host,
                    user=user, password=password, port=port, name=name, **kwargs)

def connect_to(name, node_file=None):
    '''
        finds connection specififcations via inputted config file name
    '''
    node_file = node_file or DEF_NODEFILE
    if node_file == None:
        config.load(DEF_NODEFILE) # Config() utilized to 'load' configuration file
    else:
        config.load(node_file)
    kwargs = config_for(name)

    if not kwargs:
        raise AttributeError('Device not found in ' + node_file + ' file')

    node = connect(name=name, return_node=True, **kwargs)
    return node

requests.packages.urllib3.disable_warnings()

