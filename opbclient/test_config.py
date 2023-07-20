import opb_api as api

def main():

    conn = api.connect(host='10.4.4.56',transport='https', user='admin', password='admin', port='8091')
    #conn.configFlow()
    #conn.configFlow(flow="flow1")
    #conn.configFlowRules(flow="flow1",r_id="1")
    #conn.configOverride(flow="flow1",r_id="1",dt = {"override-to": ["Ethernet7_1"],"override-push-vlan-tag": "100","override-pop-vlan": "disable"})
    conn.configAllInterfaces()
main()
