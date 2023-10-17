# Port

<strong>Import OPBNOS API</strong>

```py
import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.</p>

```py
node = opbapi.connect_to('SN2010')
```

### Configure Port Interfaces

```py
node.configAllInterfaces()
```

<p> The API configAllInterfaces() requires no parameters because the file <a href="http://127.0.0.1:8000/configJSON/#sn2010json">SN2010.json</a> contains all the required parameters in order to configure device interfaces. The content of the JSON file is in the following format:</p>
```py
        "configInterface": {
                "Ethernet1_1": {
                        "admin_status": "up",
                        "speed": "10000"
                }
```

### Configure Specific Port Interfaces

```py
node.configInterface(intf_name="Ethernet1_1")
```

<p> The API configInterface() requires one client specified parameter, intf_name, that indicates the preferred configuration parameters by referring to the appropriate request body content in the user inputted <a href="http://127.0.0.1:8000/configJSON/">JSON file</a>. The content of the JSON file should be in the following format:</p>
```py
        "configInterface": {
                "Ethernet1_1": {
                        "admin_status": "up",
                        "speed": "10000"
                }
```

<p> The below table has a list of attributes that pertain to these particular APIs: </p>
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
      <td>"admin_status"</td>
      <td>"up/down"</td>
      <td>check device activity</td>
    </tr>
    <tr>
      <td>"speed"</td>
      <td>int</td>
      <td>device speed</td>
    </tr>
    <tr>
      <td>"mtu"</td>
      <td>int</td>
      <td>maximum transmission size of an interface</td>
    </tr>
    <tr>
      <td>"fec"</td>
      <td>"none/fc/rs"</td>
      <td>forward error correction</td>
    </tr>
  </tbody>
</table>

<strong>Get/Show Port Interface</strong>
<p>Retrieves device interface elements that were previously configured.</p>

```py
node.execute(['show interfaces summary <Ethernet1_1>'])
```

<em><strong>Output</strong></em>
<p> This is an example of the output of the above command.</p>
```py
b'{"Ethernet1_1": {"admin_status": "up", "speed": "10000"}}'
```
<p> The below table is a list of out attributes pertaining to the interface get request:</p>
<table>
  <thead>
    <tr>
      <th>Attribute</th>
      <th>Values</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"lanes"</td>
      <td>"int"</td>
      <td>device data lanes</td>
    </tr>
    <tr>
      <td>"alias"</td>
      <td>"tenGigE1"</td>
      <td>alias name for port interface</td>
    </tr>
    <tr>
      <td>"oper_status"</td>
      <td>"down/up"</td>
      <td>status the port is currently operating at</td>
    </tr>
    <tr>
      <td>"admin_status"</td>
      <td>"up/down"</td>
      <td>indicates configured state of the device</td>
    </tr>
    <tr>
      <td>"speed"</td>
      <td>int</td>
      <td>device speed</td>
    </tr>
    <tr>
      <td>"mtu"</td>
      <td>int</td>
      <td>maximum transmission size of an interface</td>
    </tr>
    <tr>
      <td>"description"</td>
      <td>"N/A"</td>
      <td>any specificity descriptions</td>
    </tr>
    <tr>
      <td>"autoneg"</td>
      <td>"N/A"</td>
      <td>used to determine the optimal speed and mode of connection for two connected devices</td>
    </tr>
    <tr>
      <td>"TRANSCEIVER"</td>
      <td>"Present"</td>
      <td>indicates whether a device transceiver is present</td>
    </tr>
  </tbody>
</table>
