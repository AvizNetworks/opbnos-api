# Port Channel

**Import OPBNOS API**

```py
import opb_api as opbapi
```

**Initialize client** 
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests. </p>

```py
node = opbapi.connect_to('SN2010')
```

<strong>Configure portchannel information</strong>
<p>In order to configure portchannel information, the API, configportchannel(), must be invoked with appropriate parameters in dictionary format.</p>
```py
node.configPortChannel(pch_id="1", port_list=["Ethernet1_1","Ethernet2_1"])
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
      <td>"add_member"</td>
      <td>["Ethernet1_1", ["Ethernet2_2"],</td>
      <td>indicates the members within which the port channels are configured</td>
    </tr>
    <tr>
      <td>"description"</td>
      <td>"test"</td>
      <td>additional port channel description</td>
    </tr>
  </tbody>
</table>

<strong>Get Port information</strong>
<p>Retrieves server port details </p>
```py
node.execute(['show port-channel information'])
```
<strong>Output</strong>
<p>The output is in JSON format. </p>
<p>Note: if port channel is not configured, the device will return the below error messege:</p>
```py
b'{"[ERROR]": "PortChannel not configured!"}'
```
<p> This will be the proper JSON output if port channel information have been configured.</p>
```py
b'{"1": {"ports": ["Ethernet1_1", "Ethernet2_1"]}}'
```

<p> The below table has a list of output attributes:</p>
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
      <td>"ports"</td>
      <td>["EthernetX_X", ["EthernetY_Y"],</td>
      <td>indicates port channels configured</td>
    </tr>
    <tr>
      <td>"comment"</td>
      <td>"test"</td>
      <td>additional port channel/device related comments</td>
    </tr>
  </tbody>
</table>
