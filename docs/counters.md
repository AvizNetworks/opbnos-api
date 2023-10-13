# Counters
<p> Retrieves the performance and interface counters from OPBNOS device.</p>
<strong>Import OPBNOS API</strong>

```py
import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.</p>

```py
node = opbapi.connect_to('SN2010')
```

<strong>Get/Show Interface Counters</strong>

<p> Retrieves available performance counter</p>

```py
node.execute(['show interface counters'])
```
<strong>Output</strong>
```py
b'{"Ethernet1_1": {"IF_IN_OCTETS": 0, "IF_IN_UCAST_PKTS": 0, "IF_IN_NON_UCAST_PKTS": 0, "IF_IN_DISCARDS": 0, "IF_IN_ERRORS": 0, "IF_OUT_OCTETS": 0, "IF_OUT_UCAST_PKTS": 0, "IF_OUT_NON_UCAST_PKTS": 0, "IF_OUT_DISCARDS": 0, "IF_OUT_ERRORS": 0, "IF_IN_MULTICAST_PKTS": 0, "IF_OUT_MULTICAST_PKTS": 0}, "Ethernet2_1":{...}...}
```

### Clear Interface Counters
<p>In order to delete all interface counters, the API, configInterfacesCounters(), can be invoked with no paramters.</p>

```py
node.configInterfacesCounters()
```

<strong>Get/Show Interface Counters - Ethernet specific</strong>
<p>Retrieves Interface counter information as per the specified ethernet</p>

```py
node.execute(['show interface counters <Ethernet1_1>'])
```
<strong>Output</strong>
```py
b'{"Ethernet1_1": {"IF_IN_OCTETS": 0, "IF_IN_UCAST_PKTS": 0, "IF_IN_NON_UCAST_PKTS": 0, "IF_IN_DISCARDS": 0, "IF_IN_ERRORS": 0, "IF_OUT_OCTETS": 0, "IF_OUT_UCAST_PKTS": 0, "IF_OUT_NON_UCAST_PKTS": 0, "IF_OUT_DISCARDS": 0, "IF_OUT_ERRORS": 0, "IF_IN_MULTICAST_PKTS": 0, "IF_OUT_MULTICAST_PKTS": 0}}
```

### Clear Flow Counters
<p>In order to clear opb flow counters, the API, clearFlowCounters(), can be invoked with no paramters.</p>
```py
node.clearFlowCounters(flow="flow1", r_id="1")
```
<p> The below table lists and describes input attributes:
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
      <td>"flow"</td>
      <td>"flow1"</td>
      <td>flow identification</td>
    </tr>
    <tr>
      <td>"r_id"</td>
      <td>int</td>
      <td>rule id number</td>
    </tr>
  </tbody>
</table>

<strong>Note: Output of clear APIs</strong>
<p> APIs will not produce any output unless the below status code in produced, indicating a server error.
```py
Status : 500 -> Response : b'500'
```
