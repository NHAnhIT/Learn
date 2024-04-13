import requests
from lxml import html

headers = {
    'Cookie': 'JSESSIONID=7817702B12160EDBF57229B43D0D9F9B; _ga=GA1.1.1720943134.1711457233; _gid=GA1.1.1348886054.1711457233; _ga_MN6GLVK538=GS1.1.1711457232.1.1.1711459418.0.0.0'
}
data = {
    'fromDate': '01/01/2024',
    'toDate': '31/03/2024',
    'check': 'false',
    'curShopId': '1',
    'lstShopId': '1',
    'promotionCode': '',
    'reportCode': '1711459412377'
}
# get tree report in screen
r = requests.get('http://192.168.1.223:3600/rest/report/tree.json?id=0&name=&url=', headers=headers)
#  convert json to dict
tree_report_dict = r.json()
# get url report in dict
report_url = tree_report_dict[0]['children'][0]['children'][0]['attr']['url'] # change children 2 to change report
# request each report
r = requests.post('http://192.168.1.223:3600' + report_url, headers=headers, data=data)
# get link file to download
link_file = r.json()['path']
# request file download
r = requests.get(link_file)
# write to as file with data_type is byte
with open('1.8.1.1.xlsx', 'wb') as file:
    file.write(r.content)