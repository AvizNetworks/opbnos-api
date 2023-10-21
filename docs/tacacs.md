# TACACS

**Import OPBNOS API**

```py
import opb_api as opbapi
```

**Initialize client**
<p>Use the appropriate JSON file that corresponds to the targetted device name. This JSON file should contain request body parameters corresponding to any potential configuration/post requests.</p>

```py
node = opbapi.connect_to('SN2010')
```

## Configure TACACS Global Config
<p>In order to configure port information, the API, configTACACSglobal(), must be invoked with input parameter, 'dt'. 'dt' accepts all request body inputs in a dictionary format.</p>
```py
node.configTACACSglobal(dt = {"auth_type": "pap","timeout": 8,"passkey": "support"})
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

## Configure TACACS Server
<p>In order to configure TACACS server information, the API, configTACACSserver(), must be invoked with input parameter, 'dt'. 'dt' accepts all request body inputs in a dictionary format.</p>
```py
node.configTACACSserver(dt = {"host": "10.4.4.11","timeout": 8,"priority": 1,"auth_type": "pap","passkey": "support"})
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

<strong>Get Tacacs Server</strong>
```py
node.execute(['show tacacs-server'])
b'{"10.4.4.11": {"tcp_port": "49", "timeout": "8", "priority": "1", "passkey": "support", "auth_type": "pap"}, "global": {}}'
```

## Deletre TACACS Server
<p> In order to delete the Tacacs Server Config </p>

```py
node.deleteTACACSserver(host="10.4.4.11")
Status : 200 -> Response : b'{"Info": "TACACS server deleted successfully"}'
```


