# Counters
<p> Shows and Configures performance counters
<strong>Import OPBNOS API</strong>

```py
import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.

```py
node = opbapi.connect_to('SN2010')
```

<strong>Get/Show Interface Counters</strong>

<py>: Retrieves available performance counter

```py
node.execute(['show interface counters'])
```
<strong>Output</strong>
```py
{}
```

<strong>Get/Show SNMP Trap</strong>
<py>: Retrieves SNMP traps

```py
node.execute(['show snmp-trap'])
```
<strong>Output</strong>
```py
b'{"1": {"DestPort": "161","v2TrapDest": "Null","DestIp": "10.4.4.11","vrf": "None","Community": "public"}}
```
<py> : The API, configReboot(), reboots the system by accepting dictionary request body input to indicate authorization.

```py
node.configReboot(dt={"reboot":"yes"})
```
<strong>Output</strong>
<p> Note: Client will receive the below status codes for both deleting funtions to indicate a successful request.
```py
Status : 200 -> Response : b'200'
```
<p> The status code '500' indicates a server error.
