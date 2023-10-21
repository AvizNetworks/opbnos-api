# SNMP

<strong>Import OPBNOS API</strong>

```py
from opbclient import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.</p>

```py
node = opbapi.connect_to('SN2010')
```

## Configure SNMP community
<p>In order to configure SNMP community information, the API, configSNMPcomm(), must be invoked with appropriate parameters in dictionary format within the parameter 'dt'.</p>
```py
node.configSNMPcomm(dt="{"community":"Aviz"}")
```

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
      <td>"community"</td>
      <td>"Aviz"</td>
      <td>community string that indicates specific access data</td>
    </tr>
  </tbody>
</table>

<strong>Get/Show SNMP Community</strong>
<p> Retrieves SNMP community details</p>

```py
node.execute(['show snmp-community'])
```
<strong>Output</strong>
<p> This is an example of the output of the above command:</p>
```py
b'{"public": {"TYPE": "RO"}}'
```

## Delete SNMP Community
<p> In order to delete the SNMP Community </p>
```py
node.deleteSNMPcomm(comm="public")
```

## Configure SNMP trap
<p>In order to configure SNMP trap information, the API, configSNMPtrap(), must be invoked with appropriate parameters in dictionary format within the parameter 'dt'.</p>
```py
node.configSNMPtrap(dt="{"version":"2", "server_id":"1", "community":"public", "ip_address":"10.X.X.XX"}")
```
<p> 'dt' parameters correlate to SNMP trap messeges sent by the network devices to the system. </p>
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
      <td>"version"</td>
      <td>int</td>
      <td>version number</td>
    </tr>
    <tr>
      <td>"server_id"</td>
      <td>int</td>
      <td>server id numbers</td>
    </tr>
    <tr>
      <td>"community"</td>
      <td>"public"</td>
      <td>SNMP community string to enable acessibility</td>
    </tr>
    <tr>
      <td>"ip_address"</td>
      <td>"10.X.X.XX"</td>
      <td>system ip address</td>
    </tr>
  </tbody>
</table>

<strong>Get/Show SNMP Trap</strong>
<p> Retrieves SNMP trap details </p>

```py
node.execute(['show snmp-trap'])
```
<strong>Output</strong>
<p> This is an example of the output of the above command: </p>
```py
b'{"1": {"DestPort": "161","v2TrapDest": "Null","DestIp": "10.4.4.11","vrf": "None","Community": "public"}}'
```
<p> Note: "1": the int value in the output indicates the server id: </p>
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
      <td>"DestPort"</td>
      <td>int</td>
      <td>destination port</td>
    </tr>
    <tr>
      <td>"v2TrapDest"</td>
      <td>int/"Null"</td>
      <td>SNMPv2 trap destination</td>
    </tr>
    <tr>
      <td>"DestIp"</td>
      <td>"10.X.X.XX"</td>
      <td>destination IP</td>
    </tr>
    <tr>
      <td>"vrf"</td>
      <td>"None"</td>
      <td>indicates whether a specific VRF is associated with the trap host</td>
    </tr>
    <tr>
      <td>"Community"</td>
      <td>"public"</td>
      <td>updated configured SNMP community</td>
    </tr>
  </tbody>
</table>

## Delete SNMP Trap
<p> In order to delete the SNMP Trap with server id </p>

```py
node.deleteSNMPtrap(s_id="1")
```
