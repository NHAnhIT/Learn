import requests
from lxml import html
import json

params = {
    'u_sr_id': '59k2xIVoV5usWsUyDD97rQ6L6qiZ89aEteD9DQ9W_1710678383'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'X-Csrf-Token': 'kqzcf7IVhkJqY61AXx2D26NR1vQBfCxnrnI0B5U8',
    'Cookie': 'XSRF-TOKEN=eyJpdiI6ImFWUzhPUnZFQy8yRnRMMUhVRmVYNkE9PSIsInZhbHVlIjoiRk53V3pTRW95TXU3cjY1b25Xd2tka1dvVnkrMkdSaFNqb2QwazBpdkVxZHR0T0RaaStPY2NRelc1SmRRNTUvdFVhQlJNUHQvTGRmb0lPb2N5eHZnTTBtWUh6UWl5U2gwVGVLL2U2cDZBT2JrQWxOTnlXSk04QXZUZndjZ0xCa0MiLCJtYWMiOiIwZDFmMWVhZWQxZWYzOGM4OTllMWNmMTFmOGVjYmVlY2M0ZGZlMDI3NTgxNzQ1OTg5MzQ4ZjZlNzUyYzE0OTViIiwidGFnIjoiIn0%3D; topcv_session=eyJpdiI6ImVQNStsQldDbkhCYVovbU5jakxpU2c9PSIsInZhbHVlIjoiVDJveW1DaHQrTHRPbVcxaVZKUzZGZ1lPMHdzb2d2bjVZYllxTE5TVjZPMFZXNDVoT1EwbCsyOXRyMWlIa2JoMVhkVHVKV3ppRWg0S1dObHR0R2RlZmtPTlQxSG82VUxhNGNodTN6QWlOM3BoRE9Wa09mVWxxVGcvblJQR3l5MGoiLCJtYWMiOiI2NmY5ODNiNWQzNDI3YjljMGZjMDJhY2I3ZGI0YzAzMjhkOWE2ZThiNDdlZjIwMDRkOGJiYzc3MDk4NzkzM2JjIiwidGFnIjoiIn0%3D; appier=%7B%22event%22%3A%22job_searched%22%2C%22payload%22%3A%7B%22searched_keyword%22%3A%22business%20analyst%22%2C%22job_category%22%3A%22%22%2C%22company_category%22%3A%22%22%2C%22work_location%22%3A%22H%5Cu1ed3%20Ch%5Cu00ed%20Minh%22%7D%7D; _ga=GA1.1.564260854.1710680022; _gcl_au=1.1.1850914585.1710680024; _ga_F385SHE0Y3=GS1.1.1710680022.1.1.1710680023.59.0.0; _taid=zxa2p76AXG.1710680024723; _tafp=c8545c33d1d978406dc39b6a0aa6a359; popup-ebook-cv=1',
}

r = requests.post('https://www.topcv.vn/tim-viec-lam-business-analyst-tai-ho-chi-minh-kl2', params=params, headers=headers)
data_dict = json.loads(r.text)
search_job = data_dict['data']['html_job']
with open('c.html', 'w', encoding='utf-8') as file:
    file.write(search_job)

tree = html.fromstring(search_job.encode())
elems = tree.xpath('''//div[@class="job-list-search-result"]/div''')
print(len(elems))
title_job_str_list = []
price_str_list = []
location_str_list = []
experience_str_list = []
title_link_str_list = tree.xpath('''//h3[@class="title"]//a/@href''')
index = 0
for elem in elems:
    print(index)
    print(title_link_str_list[index])
    r = requests.get(title_link_str_list[index])
    with open('d.html', 'w', encoding='utf-8') as file:
        file.write(r.text)
    tree = html.fromstring(r.text.encode())
    title = tree.xpath('''//h1[@class="job-detail__info--title "] | //h2[@class = 'premium-job-basic-information__content--title']''')[0].text_content()
    title_job_str_list.append(title)
    print(title)
    print('-'*30)
    index += 1
    # price_str_list.extend(tree.xpath('''//div[@class="job-detail__info--section-content-value"]/text()''')[1])
    # location_str_list.extend(tree.xpath('''//div[@class="job-detail__info--section-content-value"]/text()''')[2])
    # experience_str_list.extend(tree.xpath('''//div[@class="job-detail__info--section-content-value"]/text()''')[3])
print(title_job_str_list)
# print(price_str_list)
# print(location_str_list)
# print(experience_str_list)


