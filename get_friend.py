import time
import requests 
from lxml import html


cookies = {
    'c_user': '100008166962820', 
    'xs':'41%3A03MKUOfotaJVuA%3A2%3A1712758374%3A-1%3A6233%3A%3AAcV2LSa9G6241QKkq19lml9WCV1vhChpX-t7QrJFQA'}

r = requests.get('https://mbasic.facebook.com/profile.php?id=100092286493849&v=friends', cookies=cookies)
tree = html.fromstring(r.text.encode())
name_list = tree.xpath('//h3[text() = "Friends (143)"]/following-sibling::div[1]//td[2]/a/text()')
link_acc_friend_list: list[str] = tree.xpath('//h3[text() = "Friends (143)"]/following-sibling::div[1]//td[2]/a/@href')
friend_list = []

for i in range(len(name_list)):
    data = {
            'link': 'https://mbasic.facebook.com' + link_acc_friend_list[i]
        }
    r = requests.post('https://id.traodoisub.com/api.php', data=data)
    a = r.json()
    # print(a)
    time.sleep(3)
    if 'id' in a:
        friend_list.append(r.json()['id'] + ' | ' + name_list[i])
    else:
        friend_list.append(link_acc_friend_list[i].split('id=')[1].split('&')[0] + ' | ' + name_list[i])
    print(friend_list)
    print(link_acc_friend_list[i])
friend_str = '\n'.join(friend_list)
with open('friend.txt', 'w', encoding='utf-8') as file:
    file.write(friend_str)