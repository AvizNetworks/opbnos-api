import opb_api as opbapi


def main():
    node = opbapi.connect_to('SN2010')
    #node.configFlow(flow="flow1")
    #node.configFlowRules(flow="flow1", r_id="1")
    node.configDeleteRules(flow="flow1", r_id="1")

main()
