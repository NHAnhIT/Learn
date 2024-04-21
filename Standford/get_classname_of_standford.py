import requests
import lxml.html
from lxml.html import HtmlElement

URL = 'https://web.stanford.edu/class/'
index = 100
def query_xpath(html: str, query: str) -> list[str] | list[HtmlElement]:
    return lxml.html.fromstring(html.encode()).xpath(query)

for i in range(10):
    r = requests.get(URL + 'cs' + str(index) + '/')
    if r.status_code == 404:
        print('fail')
    else:
        if r.status_code == 404 and 'title' not in r.text :
            print(index)
        else:
            query_xpath(r.text, '//title/text()')
    
    index += 1
# with open('Standford/classcode.txt', 'w') as file:
#     file.write(r.text)