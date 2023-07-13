import pyavizapi_get as avizapi

def main():

    conn = avizapi.connect(host='10.4.4.53',transport='https', user='admin', password='admin', port='8091')
    #conn.configFlow()
    conn.configFlowRules(flow="rule_id_1")

main()
