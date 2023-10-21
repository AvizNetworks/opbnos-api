# ZTP

<strong>Import OPBNOS API</strong>

```py
from opbclient import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.</p>

```py
node = opbapi.connect_to('SN2010')
```

<strong>Configure ZTP</strong>
<p>In order to enable or disable ZTP, the API, configZTP(), must be invoked with dictionary input within the object, 'dt'.</p>

```py
node.configZTP(dt = {"ztp_status":"enable | disable"})
```

<strong>Get/Show ZTP server</strong>
<p> Retrieves ZTP status</p>

```py
node.execute(['show ztp status'])
```
<strong>Output</strong>
<p> This is an example of the output of the above command:</p>
```py
b'{{"ztp-status": "disabled"}}
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
      <td>"ztp_status"</td>
      <td>"enable|disable"</td>
      <td>indicates whether ztp enable or disable on the system</td>
    </tr>
  </tbody>
</table>
