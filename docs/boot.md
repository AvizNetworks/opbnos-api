# Boot

<strong>Import OPBNOS API</strong>

```py
from opbclient import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.</p>

```py
node = opbapi.connect_to('SN2010')
```

<strong>Get System Boot information</strong>

<p> Retrieves system boot information.</p>

```py
node.execute(['show boot'])
```
<strong>Output</strong>

```py
b'{"BootInfo": {"Next": "OPBNOS-master.192-dirty-20230831.072719", "Available": "OPBNOS-master.192-dirty-20230831.072719", "Current": "OPBNOS-master.192-dirty-20230831.072719"}}'
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
      <td>"Next"</td>
      <td>"OPBNOS-master.192-dirty-20230831.072719"</td>
      <td>next boot image</td>
    </tr>
    <tr>
      <td>"Available"</td>
      <td>"OPBNOS-master.192-dirty-20230831.072719"</td>
      <td>available boot image</td>
    </tr>
    <tr>
      <td>"Current"</td>
      <td>"OPBNOS-master.192-dirty-20230831.072719"</td>
      <td>current boot image</td>
    </tr>
  </tbody>
</table>
