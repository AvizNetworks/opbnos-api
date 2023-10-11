# TACACS

**Import OPBNOS API**

```py
import opb_api as opbapi
```

**Initialize client**
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.

```py
node = opbapi.connect_to('SN2010')
```

<strong>Configure TACACS Server</strong>
<p>In order to configure TACACS server information, the API, configTACACS(), must be invoked with input parameter, 'dt'. 'dt' accepts all request body inputs in a dictionary format.
```py
node.configTACACS(dt = {"host": "10.4.4.11","timeout": 8,"priority": 1,"auth_type": "pap","passkey": "support"})
```
<p> The below table has a list of attributes that pertain to this particular API:
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
      <td>"host"</td>
      <td>"10.X.X.XX"</td>
      <td>host id</td>
    </tr>
    <tr>
      <td>"timeout"</td>
      <td>int</td>
      <td>indicates timeout value</td>
    </tr>
    <tr>
      <td>"priority"</td>
      <td>int</td>
      <td>indicates priority</td>
    </tr>
    <tr>
      <td>"auth_type"</td>
      <td>"pap"</td>
      <td>indicates authorization type (password authorization protocol)</td>
    </tr>
    <tr>
      <td>"passkey"</td>
      <td>"support"</td>
      <td>server user credential string</td>
    </tr>
  </tbody>
</table>

<strong>Configure TACACS Global Server</strong>
<p>In order to configure port information, the API, configTACACSglobal(), must be invoked with input parameter, 'dt'. 'dt' accepts all request body inputs in a dictionary format.
```py
node.configTACACS(dt = {"auth_type": "pap","timeout": 8,"passkey": "support"})
```
<p> The below table has a list of attributes that pertain to this particular API:
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
      <td>"auth_type"</td>
      <td>"pap"</td>
      <td>indicates authorization type (password authorization protocol)</td>
    </tr>
    <tr>
      <td>"timeout"</td>
      <td>int</td>
      <td>indicates timeout value</td>
    </tr>
    <tr>
      <td>"passkey"</td>
      <td>"support"</td>
      <td>server user credential string</td>
    </tr>
  </tbody>
</table>

<strong>Note: Output of APIs</strong>
<p> APIs will not produce any output unless the below status code in produced, indicating a server error.
```py
Status : 500 -> Response : b'500'
```
