# Device Configuration file

<p> A device configuration file is required in order to establish a client connection to the desired device.</p>

<p> Below is an example of the configuration file, nodeinfo.conf, with a device's, SN2010, configuration information added. 

```py
[Device:SN2010]
host: 10.4.4.53
transport: https
port: 8091
user: admin
password: admin
```

<p> The below table has a list of attributes that belong to the device configuration file: </p>
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
      <td>Device</td>
      <td>i.e. SN2010</td>
      <td>Connection device name</td>
    </tr>
    <tr>
      <td>host</td>
      <td>10.X.X.XX</td>
      <td>Host ip</td>
    </tr>
    <tr>
      <td>transport</td>
      <td>http/https</td>
      <td>transport type</td>
    </tr>
    <tr>
      <td>port</td>
      <td>i.e. 8091</td>
      <td>port number</td>
    </tr>
    <tr>
      <td>user</td>
      <td>i.e. admin</td>
      <td>client user</td>
    </tr>
    <tr>
      <td>password</td>
      <td>i.e. admin</td>
      <td>client authorization</td>
    </tr>
  </tbody>
</table>
