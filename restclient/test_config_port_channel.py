import opb_api as opbapi


def main():
    node = opbapi.connect_to('SN2010')
    #node.execute(['show port information'])
    node.configPortChannel(pch_id="1", port_list=["Ethernet1_1","Ethernet2_1"])

main()
