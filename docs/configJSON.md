# Configure Flow and Interfaces JSON file

<p> Some configure functionalities don't require API parameter inputs. Instead, they refer to a JSON file containing the required configure request body parameters.</p>

<p> The JSON file must follow the below format:
- config API specification needs to be stated. 
  - i.e. configFlow()'s request body parameters need to have an index "configFlow"
</p>

<p> This JSON file content is an example of input information for the SN2010 device (corresponding to the device name in the configuration file). This JSON file should be named 'SN2010.json'. </p> 

```py
{
        "flow1": {
                "configFlow": {
                        "status": "enable",
                        "from": ["EthernetXX_X","EthernetYY_Y"],
                        "to": ["port-channel1"]
                },

                "configRules": {
                        "1": {
                                "rule_id": "1",
                                "action": "permit",
                        },

                        "2": {
                                "rule_id": "2",
                                "action": "permit",
                                "counters": "enable"
                        }
		}
	},

        "configInterface": {
                "Ethernet1_1": {
                        "admin_status": "up",
                },
		"Ethernet2_1": {
                        "admin_status": "up",
                }
	}
}
```
