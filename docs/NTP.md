# NTP

<strong>Import OPBNOS API</strong>

```py
import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.

```py
node = opbapi.connect_to('SN2010')
```

<strong>Configure NTP server</strong>
<p>In order to configure NTP server information, the API, configNTP(), must be invoked with the server IPv4 as input parameters.
```py
node.configNTP(ip="128.123.123.123")
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
      <td>ip</td>
      <td>"128.XXX.XXX.XXX"</td>
      <td>NTP server IPv4 value</td>
    </tr>
  </tbody>
</table>

<strong>Get/Show NTP server</strong>
<p> Retrieves NTP servers details

```py
node.execute(['show ntp'])
```
<strong>Output</strong>
<p> This is an example of the output of the above command:
```py
Not added yet.
```
