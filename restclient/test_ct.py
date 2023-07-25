import opb_api as opbapi


def main():
    node = opbapi.connect_to('SN4600')
    node.execute(['show interfaces summary'])

main()
