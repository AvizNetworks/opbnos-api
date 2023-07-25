import pyaviz_get

def main():

    conn = pyaviz_get.connect(host='10.4.4.56',transport='https', user='admin', password='admin', port='8091')
    #conn.configFlow()
    conn.configFlowRules(flow="rule_id_1")

main()
