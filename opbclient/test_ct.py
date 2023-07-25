import pyavizapi_get as avizapi


def main():
    avizapi.load_config('nodeinfo.conf')
    node = avizapi.connect_to('EC-AS7712')

    node.execute(['show interfaces summary'])

main()
