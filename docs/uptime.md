# System Uptime

<strong>Import OPBNOS API</strong>

```py
import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.

```py
node = opbapi.connect_to('SN2010')
```

<strong>Get/Show System Uptime</strong>
<p> Retrieves system uptime

```py
node.execute(['show uptime'])
```
<strong>Output</strong>
<p> This is an example of the output of the above command:
```py
b'{"uptime": "01:05:51 up 26 days, 20:09,  2 users,  load average: 0.54, 0.50, 0.51"}'
```

<p> The below table lists and describes input and output attributes:
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
      <td>"uptime"</td>
      <td>"01:05:51 up 26 days, 20:09,  2 users,  load average: 0.54, 0.50, 0.51"</td>
      <td>indicates system uptime information</td>
    </tr>
  </tbody>
</table>
