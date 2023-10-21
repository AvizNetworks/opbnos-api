# Syslog information

<strong>Import OPBNOS API</strong>

```py
from opbclient import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.</p>

```py
node = opbapi.connect_to('SN2010')
```

<strong>Get/Show Syslog Information</strong>
<p> Retrieves syslogs from the system</p>

```py
node.execute(['show syslog information'])
```
<strong>Output</strong>
<p> This is an example of the output of the above command:</p>
```py
b'{"1":{"time":"Oct 5 06:22:26.453866","severity":"INFO","component":"syncd#/broadcom_nagg_asic.py","msg":"[nagr]:Stat Poll-Table Handler Key map6 Data{'clear-all': 'false'}"}'
```
<p> The below table lists possible outputs:</p>
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
      <td>"time"</td>
      <td>"Month Date time"</td>
      <td>timestamp</td>
    </tr>
    <tr>
      <td>"severity"</td>
      <td>int/"INFO"</td>
      <td>event severity rating</td>
    </tr>
    <tr>
      <td>"component"</td>
      <td>""</td>
      <td>syslog messege components</td>
    </tr>
    <tr>
      <td>"msg"</td>
      <td>""</td>
      <td>syslog messege</td>
    </tr>
  </tbody>
</table>
