# CPU Utilization

<strong>Import OPBNOS API</strong>

```py
import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.

```py
node = opbapi.connect_to('SN2010')
```

<strong>Get/Show CPU Utilization</strong>
<p> Retrieves system CPU utilization

```py
node.execute(['show cpu util'])
```
<strong>Output</strong>
<p> This is an example of the output of the above command:
```py
b'{"%CPU_Util": "14.249999999999998"}'
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
      <td>"CPU_Util"</td>
      <td>float</td>
      <td>indicates average CPU usage</td>
    </tr>
  </tbody>
</table>

<strong>Note: Output of the API</strong>
<p> API will not produce any output unless the below status code in produced, indicating a server error.
```py
Status : 500 -> Response : b'500'
```
