# System Clock

<strong>Import OPBNOS API</strong>

```py
import opb_api as opbapi
```

<strong>Initialize client</strong>
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.

```py
node = opbapi.connect_to('SN2010')
```

<strong>Get/Show Clock Information</strong>
<p> Retrieves system clock information

```py
node.execute(['show clock'])
```
<strong>Output</strong>
<p> This is an example of the output of the above command:
```py
b'{"currentTime": "Sat 07 Oct 2023 01:12:59 AM UTC"}'
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
      <td>"currentTime"</td>
      <td>"Sat 07 Oct 2023 01:12:59 AM UTC"</td>
      <td>indicates current server clock (time, date, day and timezone)</td>
    </tr>
  </tbody>
</table>

<strong>Note: Output of clock API</strong>
<p> API will not produce any output unless the below status code in produced, indicating a server error.
```py
Status : 500 -> Response : b'500'
```
