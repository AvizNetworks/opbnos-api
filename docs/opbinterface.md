# OPB Interface

**Import OPBNOS API**

```py
from opbclient import opb_api as opbapi
```

**Initialize client**
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.</p>

```py
node = opbapi.connect_to('SN2010')
```

<strong>Configure OPB Interfaces</strong>
<p>The API configInterfaceNPB() requires parameters that will serve as the request body.</p>
```py
node.configInterfaceNPB(intf_name="Ethernet16_1", igr_vlan="1000")
```
<p> The below table is a list of attributes that can be considered by clients as parameters for the OPB interface API:</p>
<p> Nvidia</p>
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
      <td>"name"</td>
      <td>"Ethernet1_1"</td>
      <td>interface name</td>
    </tr>
    <tr>
      <td>"type"</td>
      <td>"network|tool"</td>
      <td>mode of exporting device functionality</td>
    </tr>
    <tr>
      <td>"comment"</td>
      <td>"test"</td>
      <td>comments regarding interface</td>
    </tr>
    <tr>
      <td>"mode"</td>
      <td>"vlan-aware|vlan-unaware"</td>
      <td>indicates if the device is VLAN aware/enforces VLAN tagging</td>
    </tr>
    <tr>
      <td>"hybrid"</td>
      <td>"enable|disable"</td>
      <td>indicates whether the device is hybrid</td>
    </tr>
    <tr>
      <td>"ingress-vlan"</td>
      <td>"500 to 4094"</td>
      <td>adding VLAN tags to ingress packets per port</td>
    </tr>
    <tr>
      <td>"egress-tagging"</td>
      <td>"enable|disable"</td>
      <td>indicates whether the egress port is a tagged member of a VLAN</td>
    </tr>
    <tr>
      <td>"truncate-offset"</td>
      <td>"0(disable)|32-4088(multiples of 4)"</td>
      <td>truncates based on specified offset</td>
    </tr>
  </tbody>
</table>

<p> Broadcom</p>
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
      <td>"name"</td>
      <td>"Ethernet1_1"</td>
      <td>check device activity</td>
    </tr>
    <tr>
      <td>"ingress-vlan"</td>
      <td>"100"</td>
      <td>adding VLAN tags to ingress packets per port</td>
    </tr>
    <tr>
      <td>"egress-tagging"</td>
      <td>"enable|disable"</td>
      <td>indicates whether the egress port is a tagged member of a VLAN</td>
    </tr>
  </tbody>
</table>


<strong>Get/Show OPB Interface</strong>
<p>Retrieves device interface elements</p>
```py
node.execute(['show interface npb <Ethernet16_1>'])
```

<em><strong>Output</strong></em>
<p>This is an example of the output of the above command.</p>
```py
b'{"ingress-vlan": "10", "name": "Ethernet16_1", "intf_name": "Ethernet16_1"}'
```
<p> the below table contains a list of attributes that will be listed in output:</p>
<p> Nvidia</p>
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
      <td>"name"</td>
      <td>"Ethernet1_1"</td>
      <td>interface name</td>
    </tr>
    <tr>
      <td>"type"</td>
      <td>"network|tool"</td>
      <td>mode of exporting device functionality</td>
    </tr>
    <tr>
      <td>"comment"</td>
      <td>"test"</td>
      <td>comments regarding interface</td>
    </tr>
    <tr>
      <td>"mode"</td>
      <td>"vlan-aware"</td>
      <td>indicates if the device is VLAN aware/enforces VLAN tagging</td>
    </tr>
    <tr>
      <td>"ingress-vlan"</td>
      <td>"100"</td>
      <td>adding VLAN tags to ingress packets per port</td>
    </tr>
    <tr>
      <td>"egress-tagging"</td>
      <td>"enable|disable"</td>
      <td>indicates whether the egress port is a tagged member of a VLAN</td>
    </tr>
    <tr>
      <td>"truncate-offset"</td>
      <td>"0(disable)"</td>
      <td>truncates based on specified offset</td>
    </tr>
  </tbody>
</table>

<p> Broadcom</p>
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
      <td>"name"</td>
      <td>"Ethernet1_1"</td>
      <td>interface name</td>
    </tr>
    <tr>
      <td>"ingress-vlan"</td>
      <td>"100"</td>
      <td>adding VLAN tags to ingress packets per port</td>
    </tr>
  </tbody>
</table>
