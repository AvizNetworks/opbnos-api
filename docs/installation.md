# Installation

###### Please take the steps below to install OPBNOS API.

### Prerequisites
- Python version 3.7+
- pip version 21.2.4+
- Download [opbnos-api-0.1.tar.gz](https://github.com/AvizNetworks/opbnos-api/blob/master/versions/opbnos-api-0.1.tar.gz)

### Install package

```py
pip install opbnos-api-0.1.tar.gz
```

If above command does not work, try using pip3:
```py
pip3 install opbnos-api-0.1.tar.gz
```
```
tar -xzvf opbnos-api-0.1.tar.gz
cp opbnos-api-0.1/opbclient/getcmd.csv opbnos-api-0.1/opbclient/nodeinfo.conf opbnos-api-0.1/opbclient/SN2010.json .
```
Note : nodeinfo.conf and SN2010.json should be modified as per the requirement

**Logs**
```
harrish@Harrishs-MacBook-Pro PIP % ls
SN2010.json		getcmd.csv		nodeinfo.conf		opbnos-api-0.1		opbnos-api-0.1.tar.gz
harrish@Harrishs-MacBook-Pro PIP %

harrish@Harrishs-MacBook-Pro PIP % python3
Python 3.11.4 (main, Jul 25 2023, 17:36:13) [Clang 14.0.3 (clang-1403.0.22.14.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from opbclient import opb_api
>>> node=opb_api.connect_to('SN2010')
file : nodeinfo.conf. Device name : SN2010
>>> node.execute(['show platform summary'])
b'{"buffer_model": "traditional", "hostname": "sonic", "hwsku": "ACS-MSN3700C", "mac": "1c:34:da:24:de:00", "platform": "x86_64-mlnx_msn3700c-r0", "synchronous_mode": "enable", "type": "LeafRouter"}'
```
