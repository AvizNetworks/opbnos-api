# Timezone

<strong>Import OPBNOS API</strong>

```py
import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.</p>

```py
node = opbapi.connect_to('SN2010')
```

<strong>Configure Timezone</strong>
<p>In order to configure Timezone information, the API, configTimezone(), must be invoked with appropriate parameters in dictionary format within the parameter 'dt'.</p>
```py
node.configTimezone(dt = {"timezone": "Asia/Kolkata"})
```

<p> The below table lists and describes input attributes:</p>
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
      <td>"timezone"</td>
      <td>"Asia/Kolkata"</td>
      <td>indicates preferred timezone</td>
    </tr>
  </tbody>
</table>

<strong>Note: Output of clock API</strong>
<p> API will not produce any output unless the below status code in produced, indicating a server error.</p>
```py
Status : 500 -> Response : b'500'
```
