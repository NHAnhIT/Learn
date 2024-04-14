import requests
from lxml import html
cookies = {
    'c_user': '61556344384507',
    'xs': '33%3Ad8HM5A15ATmslA%3A2%3A1710514371%3A-1%3A-1'
}
r = requests.get('https://mbasic.facebook.com/groups/3272112773116278?eav=Afa9bBCz5gDMzwtKvBt7cUyhu2bfKq9gznenQw1Cirr4J-IDd-Jt89XAhxtSclHDAv0&paipv=0&_rdr', cookies=cookies)
tree = html.fromstring(r.text.encode())
link_str_list = tree.xpath('''//span[text() = 'Xem thêm bài viết']/../@href''')
r = requests.get('https://mbasic.facebook.com' + link_str_list[0], cookies=cookies)
with open('b.html', 'w', encoding='utf-8') as file:
    file.write(r.text)

print(1)