# Platform

<strong>Import OPBNOS API</strong>

```py
from opbclient import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.</p>

```py
node = opbapi.connect_to('SN2010')
```

<strong>Get/Show Platform Summary</strong>
<p> Retrieves system detailed device information </p>

```py
node.execute(['show platform summary'])
```
<strong>Output</strong>
<p> This is an example of the output of the above command:</p>
```py
b'{"mac": "80:a2:XX:XX:XX:a7", "platform": "x86_64-accton_asXXXX_XXx-rX", "hostname": "sonic", "type": "LeafRouter", "hwsku": "Accton-AS7712-32X", "buffer_model": "traditional"}'
```

<p> The below table lists and describes input and output attributes:</p>
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
      <td>"mac"</td>
      <td>"80:a2:XX:XX:XX:a7"</td>
      <td>indicates mac address</td>
    </tr>
    <tr>
      <td>"platform"</td>
      <td>"x86_64-accton_asXXXX_XXx-rX"</td>
      <td>indicates</td>
    </tr>
    <tr>
      <td>"hostname"</td>
      <td>"sonic"</td>
      <td>indicates platform hostname</td>
    </tr>
    <tr>
      <td>"type"</td>
      <td>"LeafRouter"</td>
      <td>indicates router protocol</td>
    </tr>
    <tr>
      <td>"hwksu"</td>
      <td>"Accton-AS7712-32X"</td>
      <td>indicates</td>
    </tr>
    <tr>
      <td>"buffer_model"</td>
      <td>"traditional"</td>
      <td>indicates</td>
    </tr>
  </tbody>
</table>

<strong>Get/Show Platform Environment Information</strong>
<p> Retrieves system developer environment information</p>

```py
node.execute(['show platform environment information'])
```
<strong>Output</strong>
<p> This is an example of the output of the above command:</p>
```py
b'{"Fans": {"Fan 3 Front": "7900", "Fan 1 Rear": "7100", "Fan 5 Front": "8200", "Fan 2 Rear": "7100", "Fan 1 Front": "7600", "Fan 4 Front": "7900", "Fan 6 Rear": "7000", "Fan 5 Rear": "7500", "Fan 2 Front": "7900", "Fan 6 Front": "7800", "Fan 4 Rear": "7300", "Fan 3 Rear": "7200"}, "Platform": {"SONIC_VERSION": "SONiC.master.192-dirty-20230831.072719", "ASIC": "broadcom", "HwSKU": "Accton-AS7712-32X", "SONIC_KERNEL_VERSION": "4.19.0-12-2-amd64", "OPB_NOS_VERSION": "2.6.0", "SONIC_DEBIAN_VERSION": "10.12", "Platform": "x86_64-accton_as7712_32x-r0"}, "Temperature": {"Ambient": {}, "CPU": {"Core0": 39.0, "Core2": 41.0, "Core1": 39.0, "Core3": 41.0}}}'
```

<p> The below table lists and describes input and output attributes:</p>
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
      <td>"Fans"</td>
      <td>"Fan *"</td>
      <td>indicates dev environment fan information</td>
    </tr>
    <tr>
      <td>"Platform"</td>
      <td>"SONIC_VERSION", "ASIC", "HwSKU"</td>
      <td>indicates platform information</td>
    </tr>
    <tr>
      <td>"Temperature"</td>
      <td>""</td>
      <td>indicates environment temperatures</td>
    </tr>
  </tbody>
</table>

<strong>Get/Show SSD Health information</strong>
<p> Retrieves SSD health information</p>

```py
node.execute(['show platform ssdhealth'])
```
<strong>Output</strong>
<p> This is an example of the output of the above command:</p>
```py
b'{"ssdhealth": {"Temperature": "100C", "Health": "N/A", "Device Model": "TS64EPTDE1500"}}'
```

<p> The below table lists and describes input and output attributes:</p>
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
      <td>"Temperature"</td>
      <td>"100C"</td>
      <td>indicates SSD temperature</td>
    </tr>
    <tr>
      <td>"Health"</td>
      <td>"N/A"</td>
      <td>indicates SSD health status</td>
    </tr>
    <tr>
      <td>"Device Model"</td>
      <td>"TSXXXXX"</td>
      <td>indicates SSD model number</td>
    </tr>
  </tbody>
</table>

<strong>Get/Show Platform PSU Status</strong>
<p> Retrieves system PSU information</p>

```py
node.execute(['show platform psustatus'])
```
<strong>Output</strong>
<p> This is an example of the output of the above command:</p>
```py
b'{"PSU_1": {"voltage": "12.234", "led_status": "green", "temp_threshold": "False", "current": "11.421", "model": "\\bYM-2651Y", "power": "139.0", "is_replaceable": "True", "status": "true", "temp": "31.0", "voltage_min_threshold": "11.625", "voltage_max_threshold": "12.359", "presence": "true"}, "PSU_2": {"voltage": "0.0", "led_status": "red", "temp_threshold": "False", "current": "0.0", "model": "", "power": "0.0", "is_replaceable": "True", "status": "false", "temp": "0.0", "voltage_min_threshold": "0.0", "voltage_max_threshold": "0.0", "presence": "true"}}'
```

<strong>Get/Show Platform EEPROM Status</strong>
<p> Retrieves system EEPROM information</p>

```py
node.execute(['show platform syseeprom'])
```
<strong>Output</strong>
<p> This is an example of the output of the above command:</p>
```py
b'{{"EEPROM_INFO|0x24": {"Value": "1C:34:DA:36:F7:80","Name": "Base MAC Address","Len": "6"},
"EEPROM_INFO|State": {"Initialized": "1"},"EEPROM_INFO|0xfd": {"Value_4": "","Value_1": "","Len_0": "36","Value_2": "","Len_2": "36","Name_4": "Vendor Extension","Len_1": "164","Name_0": "Vendor Extension","Value_0": "","Name_2": "Vendor Extension","Name_3": "Vendor Extension","Num_vendor_ext": "5","Len_3": "36","Len_4": "36","Value_3": "","Name_1": "Vendor Extension"}}'
```

<p> The below table lists and describes input and output attributes:</p>
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
      <td>"EEPROM_INFO|0xef"</td>
      <td>{}</td>
      <td>indicated EEPROM information</td>
    </tr>
    <tr>
      <td>"Value"</td>
      <td>"1C:34:DA:36:F7:80"</td>
      <td>indicates </td>
    </tr>
    <tr>
      <td>"Name"</td>
      <td>"Base MAC Adddress"</td>
      <td>indicates </td>
    </tr>
    <tr>
      <td>"Len" or "Total Length"</td>
      <td>"6"</td>
      <td>indicates available bytes/total bytes</td>
    </tr>
    <tr>  
      <td>"Value"</td>
      <td>""</td>
      <td>indicates stored EEPROM values</td>
    </tr>
    <tr>
      <td>"Vendor Name"</td>
      <td>""</td>
      <td>indicates stored EEPROM vendor name/value</td>
    </tr>
  </tbody>
</table>

<strong>Note: Output of clock API</strong>
<p> API will not produce any output unless the below status code in produced, indicating a server error.</p>
```py
Status : 500 -> Response : b'500'
```
