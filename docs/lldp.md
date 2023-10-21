# LLDP

<strong>Import OPBNOS API</strong>

```py
from opbclient import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.</p>

```py
node = opbapi.connect_to('SN2010')
```

<strong>Get/Show Memory Utilization</strong>
<p> Retrieves system LLDP-neighbor information</p>

```py
node.execute(['show lldp neighbours'])
```
<strong>Output</strong>
<p> This is an example of the output of the above command:</p>
```py
b'{"Ethernet28_1": {"chassis": {"sonic": {"capability": [{"type": "Bridge", "enabled": true}, {"type": "Router", "enabled": true}, {"type": "Wlan", "enabled": false}, {"type": "Station", "enabled": false}], "id": {"value": "80:a2:35:57:49:a7", "type": "mac"}, "descr": "SONiC Software Version: SONiC.master.192-dirty-20230831.072719 - HwSku: Accton-AS7712-32X - Distribution: Debian 10.12 - Kernel: 4.19.0-12-2-amd64", "mgmt-ip": ["10.4.4.56"]}}, "age": "26 days, 20:53:04", "rid": "1", "via": "LLDP", "port": {"ttl": "120", "id": {"value": "hundredGigE30", "type": "local"}, "descr": "Ethernet30/1"}}, "time_stamp": "09:10:23 02:05:31Z", "Ethernet30_1":...}
```
