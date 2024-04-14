import requests
from lxml import html

ID_GROUP = '3272112773116278'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin'
}

cookies = {
    'c_user': '61556025227725',
    'xs': '26%3ASLV0k52OmZG0Ww%3A2%3A1710574490%3A-1%3A-1'
}

r = requests.get('https://mbasic.facebook.com/' + ID_GROUP, cookies=cookies)


with open('a.html', 'w', encoding='utf-8') as file:
    file.write(r.text)
result_list = []
link_share_post_list = []
current_page = 0
while True:
    current_page += 1
    print(current_page)
    
    # with open('a.html', 'w', encoding='utf-8') as file:
    #     file.write(r.text)
    tree = html.fromstring(r.text.encode())
    elems = tree.xpath('''//div[@data-ft='{"tn":"*s"}']''')
    content_in_post_list = []
    key_jobs_list = ['BA', 'BI', 'Business Analyst', 'Business Intelligence']
    location = ['HCM', 'Hồ Chí Minh']
    index = 0
    for elem in elems:
        content_in_post_list.append(str(elem.text_content()))
    for content in content_in_post_list:
        for l in location:
            if l in content:
                for key_job in key_jobs_list:
                    if key_job in content:
                        result_list.append(content)
                        link_share_post_list.append(tree.xpath('''//a[text() = 'Chia sẻ']/@href''')[index])
        index += 1
    str_list = tree.xpath('''//h3[text() = 'Hoạt động mới nhất']/following-sibling::div//abbr[contains(text(), 'tháng 2')]''')
    if str_list != []:
        break
    link_str_list = tree.xpath('''//span[text() = 'Xem thêm bài viết']/../@href''')
    print(link_str_list)
    r = requests.get('https://mbasic.facebook.com' + link_str_list[0], cookies=cookies)
    
print(result_list)
# share post
for link_share in link_share_post_list[:3]:
    r = requests.get('https://mbasic.facebook.com' + link_share, cookies=cookies)
    post_url = r.text.split('<form method="post" action="')[1].split('"')[0].replace('amp;', '')
    fb_dtsg = r.text.split('name="fb_dtsg" value="')[1].split('"')[0]
    target = r.text.split('name="target" value="')[1].split('"')[0]
    sid = r.text.split('name="sid" value="')[1].split('"')[0]
    data = {
        'fb_dtsg': fb_dtsg,
        'target': target,
        'c_src': 'share',
        'referrer': 'group',
        'privacyx': '300645083384735',
        'sid': sid,
        'view_post': 'Chia sẻ',
    }
    r = requests.post('https://mbasic.facebook.com' + post_url, data=data, cookies=cookies)

with open('a.html', 'w', encoding='utf-8') as file:
    file.write(r.text)

