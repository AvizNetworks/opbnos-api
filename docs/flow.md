# Flow

<strong>Import OPBNOS API</strong>

```py
import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.

```py
node = opbapi.connect_to('SN2010')
```

<strong>Configure flow information</strong>
<p>In order to configure port information, the API, configFlow(), must be invoked with appropriate parameters in dictionary format.
```py
node.configFlow(flow = "flow1")
```

<p> The API configFlow() requires only one parameter (flow alias) because the file SN2010 contains all the required request body parameters in order to configure device flow. The content of the JSON file is in the following format:
```py
        "flow1": {
                "configFlow": {
                        "alias": "flow1",
                        "status": "enable",
                        "comment": "vlan traffic test",
                        "from": ["Ethernet16_1","Ethernet17_1"],
                        "to": ["port-channel1"]
                }
```

<p> The below table has a list of attributes that pertain to this particular API:
<table>
 <tbody>
  <thead>
    <tr>
      <th>Attribute</th>
      <th>Values</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"alias"</td>
      <td>"flow1"</td>
      <td>alias name for flow</td>
    </tr>
    <tr>
      <td>"status"</td>
      <td>"enable|disable"</td>
      <td>indicates device status</td>
    </tr>
    <tr>
      <td>"comment"</td>
      <td>"test"</td>
      <td>additional port channel/device related comments</td>
    </tr>
    <tr>
      <td>"from"</td>
      <td>["EthernetX_X"]</td>
      <td>indicates device requesting flow authorization</td>
    </tr>
    <tr>
      <td>"to"</td>
      <td>["EthernetY_Y"]</td>
      <td>indicates device that recieves/directs authorization</td>
    </tr>
    <tr>
      <td>"push-vlan"</td>
      <td>"vlan-id"</td>
      <td>pushing VLAN tags</td>
    </tr>
    <tr>
      <td>"pop-vlan"</td>
      <td>"enable|disable"</td>
      <td>popping/removing VLAN tags</td>
    </tr>
  </tbody>
</table>

<strong>Configure flow rule information</strong>
<p>In order to configure port information, the API, configFlow(), must be invoked with appropriate parameters in dictionary format.
```py
node.configFlowRules(flow = "flow1", r_id = "1")
```

<p> The API configFlowRules() requires two parameters (flow alias and rule id) because the file SN2010 contains all the required request body parameters in order to configure device flow. The content of the JSON file is in the following format:
```py
        "flow1": {
                "configRules": {
                        "1": {
                                "rule_id": "1",
                                "action": "permit",
                                "vlan": "100",
                                "counters": "enable"
                        }
		}
	}

```

<p> The below table has a list of attributes that can be listed in the JSON file (in this case 'SN2010'):
<table>
 <tbody>
  <thead>
    <tr>
      <th>Attribute</th>
      <th>Values</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"alias"</td>
      <td>"flow1"</td>
      <td>alias name for flow</td>
    </tr>
    <tr>
      <td>"status"</td>
      <td>"enable|disable"</td>
      <td>indicates device status</td>
    </tr>
    <tr>
      <td>"comment"</td>
      <td>"test"</td>
      <td>additional flow channel/device related comments</td>
    </tr>
    <tr>
      <td>"vlan"</td>
      <td>int</td>
      <td>VLAN port number</td>
    </tr>
    <tr>
      <td>"ethertype"</td>
      <td>"0x8100"</td>
      <td>indicates protocol in Ethernet frame</td>
    </tr>
    <tr>
      <td>"src_ip"</td>
      <td>"1.1.1.1"</td>
      <td>source ip address</td>
    </tr>
    <tr>
      <td>"src_mask"</td>
      <td>"255.XXX.XXX.0"</td>
      <td>source masking ip</td>
    </tr>
    <tr>
      <td>"dst_ip"</td>
      <td>"2.2.2.2"</td>
      <td>destination ip address</td>
    </tr>
    <tr>
      <td>"dst_mask"</td>
      <td>"255.YYY.YYY.0"</td>
      <td>destination ip masking</td>
    </tr>
    <tr>
      <td>"dscp"</td>
      <td>"5"</td>
      <td>dscp code (network traffic)</td>
    </tr>
    <tr>
      <td>"ttl"</td>
      <td>"4"</td>
      <td>'time to live'</td>
    </tr>
    <tr>
      <td>"protocol"</td>
      <td>"6"</td>
      <td>protocol code</td>
    </tr>
    <tr>
      <td>"src_l4port"</td>
      <td>"56"</td>
      <td>source port number</td>
    </tr>
    <tr>
      <td>"dst_l4port"</td>
      <td>"78"</td>
      <td>destination port code</td>
    </tr>
    <tr>
      <td>"tcpctl"</td>
      <td>"0xX"</td>
      <td>tcp control</td>
    </tr>
    <tr>
      <td>"tcpctl_mask"</td>
      <td>"0xff"</td>
      <td>tcp control filter mask</td>
    </tr>
    <tr>
      <td>"tosval"</td>
      <td>"3"</td>
      <td></td>
    </tr>
    <tr>
      <td>"match_all"</td>
      <td>"disable|enable"</td>
      <td>indicates the status of </td>
    </tr>
    <tr>
      <td>"counters"</td>
      <td>"enable|disable"</td>
      <td>Indicates the status of device related performance counters</td>
    </tr>
  </tbody>
</table>

<strong>Get/Show Flow</strong>
<py> Retrieves device flow information with an 'alias'

```py
node.execute(['show flow alias <alias>'])
```
<strong>Output</strong>
<p> Note: Client will receive the below error messege if flow has not been configured.
```py
b'{"[ERROR]": "Flow not configured!"}'
```

<p> This will be the proper JSON output format if flow has been configured
```py
b'{"flow1|1": {"name": "flow1", "status": "enable", "to": ["Ethernet16_1"], "from": }}'
```

<p> The below table has a list of attributes that will appear as get flow output:
<table>
 <tbody>
  <thead>
    <tr>
      <th>Attribute</th>
      <th>Values</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"name"</td>
      <td>"flow1"</td>
      <td>alias name for flow</td>
    </tr>
    <tr>
      <td>"status"</td>
      <td>"enable|disable"</td>
      <td>indicates device status</td>
    </tr>
    <tr>
      <td>"config_mgr"</td>
      <td>"Rest-API"</td>
      <td>name of configuration manager</td>
    </tr>
    <tr>
      <td>"to"</td>
      <td>["EthernetX_X"]</td>
      <td>indicates device that recieves/directs authorization</td>
    </tr>
    <tr>
      <td>"from"</td>
      <td>["EthernetY_Y"]</td>
      <td>indicates device requesting flow authorization</td>
    </tr>
    <tr>
      <td>"comment"</td>
      <td>"vlan traffic test"</td>
      <td>additional vlan/flow/device related comments</td>
    </tr>
  </tbody>
</table>

<strong>Delete Flow</strong>
<p>In order to delete flow, the API, configDelete(), must have one parameter specifing the targetted flow alias. 
```py
node.configDelete(flow = "flow1")
```
<strong>Delete Flow Rule Override</strong>
<p> This is a multifunctional API that deletes all present flow rules and configures a new flow rule based on user specified input.
```py
node.configDelete(flow = "flow1", r_id = 1)
```

<strong>Output</strong>
<p> Note: Client will receive the below status codes for both deleting funtions to indicate a successful request.
```py
Status : 200 -> Response : b'200'
```
<p> The status code '500' indicates a server error. 

