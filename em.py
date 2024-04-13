import json
import requests

cookie = {
    '_ga': 'GA1.1.1035099940.1685415145',
    '_ga_QGMSSBR4ZC': 'GS1.1.1708338866.7.0.1708338866.0.0.0',
    'buyLevel29': '"<1"',
    '_gid': 'GA1.1.897991311.1710724869' ,
    'JSESSIONID': '634F26529B692E67E3E308306707C108',
    '_ga_MN6GLVK538': 'GS1.1.1711070267.158.1.1711071798.0.0.0',
    'TawkConnectionTime': '0',
    'twk_uuid_5f88047e2901b92076939ef1': '%7B%22uuid%22%3A%221.1vX33GzeCYMCKfb3UVlmeI5eczWWKQVNVaW7ZqqCvaOoq77OoOQ9KB3Dt4YG6BGnpxVIqUyxWl2i4No0ilNaRd7OusfTlMdlL81AQS3k12l4ulFnhgaLRZo%22%2C%22version%22%3A3%2C%22domain%22%3A%22192.168.1.223%22%2C%22ts%22%3A1711071799301%7D'
}
datas = {
    'strListShopId': '245',
    'fromDate': '01/03/2024',
    'toDate': '21/03/2024',
    'cycleId': '20240301',
    'reportCode': '1711071746264',
    'warehouseId': '0'
}
r = requests.post('http://192.168.1.223:3600/report/stock/xntct/export', cookies=cookie, data=datas)
print(r.text)