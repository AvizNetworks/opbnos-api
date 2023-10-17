import opb_api as opbapi


def main():
    node = opbapi.connect_to('SN2010')
    node.configInterfaceNPB(intf_name="Ethernet16_1", igr_vlan="1000")

main()
