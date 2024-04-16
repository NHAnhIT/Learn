import time
import requests 
from lxml import html

ACCOUNT = ['/dieu.tran.ChuyenGia.PT.Coach?eav=AfZgbLP4BmkEw070xitbYZT62C2_bEE80XDVZ-6zQE6lCoWovk-xTy_vyoXVGlg1-Q8&fref=fr_tab&paipv=0', '100092286493849', 'Perry.Mignon/friends']
cookies = {
    'c_user': '61556578826213', 
    'xs':'32%3ARW6qv-LRbv-0jw%3A2%3A1712994138%3A-1%3A-1'
    }
for acc in ACCOUNT:
    r_account = requests.get('https://ffb.vn/api/tool/get-id-fb?idfb=https://mbasic.facebook.com/' + acc)
    print(r_account.json()['id'])
    if type(r_account.json()['id']) is str:
        r_html = requests.get('https://mbasic.facebook.com/profile.php?id=' + r_account.json()['id'] + '&v=friends', cookies=cookies)
    else: 
        r_account = requests.get('https://ffb.vn/api/tool/get-id-fb?idfb=https://mbasic.facebook.com/' + acc)
        r_html = requests.get('https://mbasic.facebook.com/profile.php?id=' + r_account.json()['id'] + '&v=friends', cookies=cookies)
    tree = html.fromstring(r_html.text.encode())
    if 'No friends to show' in r_html.text:
        print("The account has not friends or Private Friends")
    else:
        name_list = tree.xpath('//h3[contains(text(), "Friends (")]/following-sibling::div[1]//td[2]/a/text()')
        link_acc_friend_list: list[str] = tree.xpath('//h3[contains(text(), "Friends (")]/following-sibling::div[1]//td[2]/a/@href')
        friend_list = []
        while True:
            for i in range(len(name_list[:1])):
                r_link = requests.get('https://ffb.vn/api/tool/get-id-fb?idfb=https://mbasic.facebook.com' + link_acc_friend_list[i])
                if type(r_link.json()['id']) is str:
                    friend_list.append(r_link.json()['id'] + ' | ' + name_list[i])
                else:
                    r_link = requests.get('https://ffb.vn/api/tool/get-id-fb?idfb=https://mbasic.facebook.com' + link_acc_friend_list[i])
                    friend_list.append(r_link.json()['id'] + ' | ' + name_list[i])
                print(name_list[i])
            # friend_str = '\n'.join(friend_list)
            print(0)
            if 'See more friends' in r_html.text:
                tree = html.fromstring(r_html.text.encode())
                link_sm_list = tree.xpath('//div[@id = "m_more_friends"]/a/@href')
                r_click_sm = requests.get('https://mbasic.facebook.com' + link_sm_list[0], cookies=cookies)
                r_html = r_click_sm
                with open('a.html', 'w', encoding='utf-8') as file:
                    file.write(r_html.text)
                tree = html.fromstring(r_html.text.encode())
                name_list = tree.xpath('//h3[contains(text(), "Friends (")]/following-sibling::div[1]//td[2]/a/text()')
                link_acc_friend_list: list[str] = tree.xpath('//h3[contains(text(), "Friends (")]/following-sibling::div[1]//td[2]/a/@href')
                print(1)
            else: 
                break
        friend_str = '\n'.join(friend_list)
        with open('friends.txt', 'w', encoding='utf-8') as file:
            file.write(friend_str)
