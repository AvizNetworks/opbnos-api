#print device info

import opb_api as opbapi


def main():
    node = opbapi.connect_to('SN2010')
    node.execute(['show platform summary'])

main()
