
##nodeinfo.conf Parameters
###Configuration file

####Configuration options for node entries:

Device name: The device identification name  
Host: The IP address. Default parameter available.   
Username: The OBP-NOS username for authentication.   
Password: The OPB-NOS password for authentication.  
Transport: The type of transport  
Supports ‘https’ only (default parameter)  
Port: The port number used for connection. Default parameter available.   
Default port: ‘443’  

####Using HTTPS

Example ‘nodeinfo.conf’ file contents: 

```bash
[Devide:SN2010]
host: 10.4.4.53
transport: https
port: 8091
user: admin
password: admin
```
####Requirements

Python 3.7+   
Requires the Python requests module

###Module

####Api_utils

class api_utils.GetAPI(object)  

The GetAPI class creates get request from object parameters  
```bash
object -   
	host : host ip address  
	transport : currently only supports ‘https’  
	port :   
	Username, password  
```

####response(ano)

ano : get request related url path 

Support general REST get request

This method frames a get request url and adds the corresponding path. Python ‘requests’ package is then utilized to execute get request and print ‘json’ formatted output. 

####resp_arg1(ano, add)

ano : get request related url path
add : user specified url parameter

Supports REST get request involving user specified url parameters

This method frames a get request url, adds its corresponding path and a user specified parameters. A get request is executed and output printed.

####resp_arg2(ano, add)

ano : url path (multiple get request path arguments)  
add : user specified url parameter  

Supports REST get request involving user specified url parameters

This method frames a get request url, formats and adds its corresponding path arguments. A get request is executed and output printed.

####Opb_api

class opb_api.Config(SafeConfigParser)

The Config class contains methods that aid in configuration file parsing.

filename - configuration filename

####read(filename)

filename : configuration filename

Python ‘configparser’ module method ‘read’ utilized to parse through configuration file

####get_device(name)

name : user input device name

Parses through configuration file contents to retrieve device attributes from user input of device name

####load(filename)

filename : configuration file name 

Calls read() method in order to read configuration file

####method opb_api.config_for(name)

name : user input device name

Returns device connection attributes based on device name in configuration file (calls opb_api.Config.get_device)

```bash
class opb_api.Connect(object)
object - 
	host : host ip address
	transport : currently only supports ‘https’
	port : 
	user : username (ex. ‘admin’)
pass : password (ex. ‘admin’)
name : device name + concatenated with “.json” string; form post request body parameters ‘json’ filename
```
cmds, func, key (commands, function, key): lists with get parameters after reading ‘csv’ file 

device_conf : post request body parameters ‘json’ file reader

str_to_class(str)

####str : string 

Converts string data type to class type

####execute(commands)

commands : Get request CLI commands 

Parses through CLI commands and stores formatted strings in lists

####get_execute(com_spl, uni_com)

com_spl , uni_com : formatted CLI command strings (list data type) 

Retrieves lists, and performs further string formatting. Error handles invalid CLI inputs.

####api_calls(in_cmd, for_var)

str : string 

Compares formatted commands within input variables and utilizes them to get directed to appropriate get request path values in ‘csv’ file via indexing(api_utils.GetAPI)

####configFlow(flow)

flow : config flow name (ex. ‘flow1’)

Config flow method.  
Formats post request url. Retrieves post request body from device ‘json’ file by indexing flow name input and calls opb_api.Connect.request.

####configFlowAllRules(flow)

flow : config flow name

Config all flow rules. Formats post request url and calls opb_api.Connect.request.

####configFlowRules(flow, r_id)

flow : config flow name  
r_id : rule id (ex. ‘1’)

Config specific input rule in flow  
Formats post request url. Retrieves post request body from device ‘json’ file by indexing flow name input and calls opb_api.Connect.request.

####deleteAndConfigFlowRule(flow, r_id)

flow : config flow name  
r_id : rule id (ex. ‘1’)

Deletes all flows and configures specific rule in flow  
Formats delete all flows url and post requests delete requests. Then, configures a new flow and rule from user input and calls opb_api.Connect.request.

####configOverride(flow, r_id, dt)

flow : config flow name
r_id : rule id (ex. ‘1’)
dt : user data input (dictionary data type)

Overrides specific rules in flow. Post request body parameters in user input ‘dt’ object.   
Formats post requests url and calls opb_api.Connect.request with ‘dt’ as parameter.

####configDelete(flow)

flow : config flow name

Deletes all flow input. Formats post request url and calls opb_api.Connect.request.  

configDeleteRules(flow, r_id)  

flow : config flow name  
r_id : rule id (ex. ‘1’)  

Deletes specific flow rules. Formats post request url and calls opb_api.Connect.request. 

####configPortChannel(pch_id, port_list, dt, dsp)  

```bash
pch_id : port channel id  
port_list : port list  
dt : user data input (dictionary data type)  
dsp : description (optional)  
```
Configure port channel. Formats post request url and calls opb_api.Connect.request.    

####configInterface(intf_name)

intf_name : interface name   

Configures interface. Formats post request url, retrieves post request body from device ‘json’ file by indexing flow name input and calls opb_api.Connect.request. 

####configAllInterfaces()

Configure all interfaces. Formats post request url, retrieves post request body from device ‘json’ file by indexing flow name input and calls opb_api.Connect.request. 

####configInterfaceNPB(dt, intf_name, igr_vlan, egr_tag)

```bash
dt : user data input (dictionary data type)
intf_name : interface name (optional)
igr_vlan : (optional)
egr_tag : (optional)
```
Formats post request url and calls opb_api.Connect.request with ‘dt’ as parameters.

####configFlowCounters(flow, r_id)

flow : config flow name  
r_id : rule id (ex. ‘1’)  

Clears flow counters, depending on whether flow name or rule id was added or omitted as input. Formats post request url and calls opb_api.Connect.request.  

####configInterfacesCounters()

Clears all interface counters. Formats post request url and calls opb_api.Connect.request. 

####configReboot(dt)  

dt : user data input (dictionary data type)  

Configures device reboot. Formats post request url and calls opb_api.Connect.request. 

####configZTP(dt)

dt : user data input (dictionary data type)

Configures zero-touch provisioning (ZTP). Formats post request url and calls opb_api.Connect.request.

####configSNMP(dt)

dt : user data input (dictionary data type)  

Configures/sends SNMP trap using dt data input. Formats post request url and calls opb_api.Connect.request.

####configSNMPcomm(dt)  

dt : user data input (dictionary data type)  

Configure SNMP community string. Formats post request url and calls opb_api.Connect.request.

####configSNMPthreshold(dt)

dt : user data input (dictionary data type)

Configures SNMP threshold levels according to dt data input. Formats post request url and calls opb_api.Connect.request.

####configSNMPusers(dt)

dt : user data input (dictionary data type)

Configures SNMP user credentials using ‘dt’ data input. Formats post request url and calls opb_api.Connect.request.

####configTACACS(dt)

dt : user data input (dictionary data type)

Configures TACACS+ related protocols using ‘dt’ data input. Formats post request url and calls opb_api.Connect.request.

####configTACACSglobal(dt)

dt : user data input (dictionary data type)

Configures TACACS+ related protocols with global key using ‘dt’ data input. Formats post request url and calls opb_api.Connect.request.

####configNTP(ip)  

ip : network ip address  

Configures NTP (Network Time Protocol) using network ip address. Formats post request url and calls opb_api.Connect.request.

####configTimezone(dt)

dt : user data input (dictionary data type)

Configures device timezone. Formats post request url and calls opb_api.Connect.request.

####configTXEnable()

Configures tx-enable signal. Formats post request url and calls opb_api.Connect.request.

####request(dt)

dt : user data input (dictionary data type)  

Executes post request and prints status code output.  

If ‘dt’ input is Nonetype, the post request is framed using a self-stored url. If ‘dt’ has other content in the form of a dictionary, post request is framed using ‘dt’ request body information. Output in the form of a status code: ‘202’ = accepted, ‘404’ = failure

```bash
method connect(host, name, transport, user, password, port)

host = host ip address
name = device name
transport = ‘https’ supported
user = username
password = password
port = port number
```
Creating a connection via connect method requires input for all attributes. Default values provided for port, transport, and host. 

####method connect_to(name, node_file)

name : device name
node_file : configuration file name

Creating a device connection via connect_to method requires user inputted configuration file as well as targeted device name. Method retrieves credentials from device name key in configuration file and returns them in an object to connect method. 

####Configuration / Usecase Example

Establishing node connection via configuration file 

	import opb_api as opbapi
	node = opbapi.connect_to(‘SN2010’)

‘Connect_to’ module :   
	Device name string  
	‘node_file’ - configuration file name (Default configuration file - ‘nodeinfo.conf’)  


Get module use case -  
node.execute([‘show platform status’])  
JSON example output:   

```bash
b'{'buffer model": "traditional",
"hostname": "sonic",
"platform":
"X86_64-minx_msn2010-r0"
"hwsku"; "ACS-MSN2010", "mac": "1c:34: da:38:bb:80"
"synchronous mode": "enable"
"type":
"LeafRouter"}'
```





