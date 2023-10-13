# Flow

<strong>Import OPBNOS API</strong>

```py
import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.</p>

```py
node = opbapi.connect_to('SN2010')
```

### Configure flow information
<p>In order to configure flow information, the API, configFlow(), must be invoked with appropriate parameters in dictionary format.</p>
```py
node.configFlow(flow = "flow1")
```

<p> The API configFlow() requires only one parameter (flow alias) because the file <a href="http://127.0.0.1:8000/configJSON/">SN2010.json</a> contains all the required request body parameters in order to configure device flow. The content of the JSON file is in the following format:</p>
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

<p> The below table has a list of attributes that pertain to this particular API:</p>
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
      <td>indicates network ports</td>
    </tr>
    <tr>
      <td>"to"</td>
      <td>["EthernetY_Y"]</td>
      <td>indicates tool ports</td>
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

### Configure flow rule information
<p>In order to configure flow information, the API, configFlow(), must be invoked with appropriate parameters in dictionary format.</p>
```py
node.configFlowRules(flow = "flow1", r_id = "1")
```

<p> The API configFlowRules() requires two parameters (flow alias and rule id) because the file <a href="http://127.0.0.1:8000/configJSON/">SN2010.json</a> contains all the required request body parameters in order to configure device flow. The content of the JSON file is in the following format:</p>
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

<p> The below table has a list of attributes that can be listed in the JSON file (in this case 'SN2010'):</p>
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
      <td>VLAN ID</td>
    </tr>
    <tr>
      <td>"ethertype"</td>
      <td>"0x8100"</td>
      <td>indicates Ethertype in Ethernet frame</td>
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
      <td>destination port number</td>
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
      <td>Type of Service Value</td>
    </tr>
    <tr>
      <td>"match_all"</td>
      <td>"disable|enable"</td>
      <td>Match all the traffic flowing through</td>
    </tr>
    <tr>
      <td>"counters"</td>
      <td>"enable|disable"</td>
      <td>Statistics/Counters Enable or Disable</td>
    </tr>
  </tbody>
</table>

### Configure Flow All Rules information
<p>In order to configure all the rules part of a flow added in config file, the API - configFlowAllRules() can be used.</p>
```py
node.configFlow(flow = "flow1")
```

### Configure flow Override information
<p>In order to override any information for a particular rule, the API - configOverride(), must be invoked with appropriate parameters in dictionary format.</p>
```py
node.configFlow(flow = "flow1", r_id=1, dt={"override-to":["Ethernet6_1","Ethernet7_1"],"override-push-vlan-tag":"100","override-pop-vlan":"disable"})
```
<p> The below table has a list of attributes that pertain to this particular API:</p>
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
      <td>"override-to"</td>
      <td>"Interface list. Eg ["Ethernet6_1","Ethernet7_1"]"</td>
      <td>Tool ports override for particular flow</td>
    </tr>
    <tr>
      <td>"override-push-vlan-tag"</td>
      <td>"500 to 4094"</td>
      <td>Push Vlan ID override for particular rule</td>
    </tr>
    <tr>
      <td>"override-pop-vlan"</td>
      <td>"enable/disable"</td>
      <td>POP Vlan Behavior override for particular rule</td>
    </tr>
  </tbody>
</table>


<strong>Get/Show Flow</strong>
<p> Retrieves device flow information with an 'alias'</p>

```py
node.execute(['show flow alias <alias>'])
```
<strong>Output</strong>
<p> Note: Client will receive the below error messege if flow has not been configured.</p>
```py
b'{"[ERROR]": "Flow not configured!"}'
```

<p> This will be the proper JSON output format if flow has been configured</p>
```py
b'{"flow1|1": {"name": "flow1", "status": "enable", "to": ["Ethernet16_1"], "from": ["Ethernet14_1"]}}'
```

<p> The below table has a list of attributes that will appear as get flow output:</p>
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
      <td>tool ports</td>
    </tr>
    <tr>
      <td>"from"</td>
      <td>["EthernetY_Y"]</td>
      <td>network ports</td>
    </tr>
    <tr>
      <td>"comment"</td>
      <td>"vlan traffic test"</td>
      <td>additional flow/device related comments</td>
    </tr>
  </tbody>
</table>

### Delete and Config Rule
<p> This is a multifunctional API that deletes particular rule of given flow and configures a new flow rule based on user specified input.</p>
```py
node.deleteAndConfigFlowRule(flow = "flow1", r_id = 1)
```

### Delete Rule
<p>In order to delete Rule of any specific flow, the API, configDeleteRules(), must have parameters specifing the targetted flow alias and rule id as below. </p>
```py
node.configDeleteRules(flow = "flow1", r_id = 1)
```
### Delete Flow
<p>In order to delete flow, the API, configDelete(), must have one parameter specifing the targetted flow alias.</p>
```py
node.configDelete(flow = "flow1")
```

<em><strong>Output</strong></em>
<p> Note: Client will receive the below status codes for both deleting funtions to indicate a successful request.
```py
Status : 200 -> Response : b'200'
```
<p> The status code '500' indicates a server error. 

