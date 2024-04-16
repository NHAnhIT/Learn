from requests import Session
import lxml
from lxml.html import HtmlElement
import requests
from yarl import URL

XPATH_URL_FRIENDS = "//div[@id='root']/div/div/div/table//td/a"


def string_to_dict(string: str):
    return {
        k.lstrip(): v
        for k, v in (cookie.split("=") for cookie in string.rstrip("; ").split(";"))
    }


def query_xpath(html: str, query: str) -> list[str] | list[HtmlElement]:
    return lxml.html.fromstring(html.encode()).xpath(query)


def get_uid_from_url(url: str):
    origin_url = URL(url)
    if "id" in origin_url.query:
        return origin_url.query["id"]
    new_url = (
        URL("https://m.facebook.com/")
        .with_path(origin_url.path)
        .with_query(origin_url.query)
    )
    r = requests.get(
        new_url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Sec-Fetch-Site": "same-origin",
        },
    )
    if 'content="fb://profile/' in r.text:
        return r.text.split('content="fb://profile/')[1].split('"')[0]

    data_dict = requests.post('https://id.traodoisub.com/api.php', data={'link': new_url}).json()
    if 'id' in data_dict:
        print('ok')
        return data_dict['id']
    print(data_dict)
    return requests.get('https://ffb.vn/api/tool/get-id-fb', params={'idfb': new_url}).json()['id']


BASE_URL = URL("https://mbasic.facebook.com")
COOKIE = "sb=iesHZmjH-DdUpx3760LcZhhc; datr=iesHZklczNwEWExGA_fJzwR-; c_user=100007681321904; wd=1920x911; ps_n=0; ps_l=0; xs=1%3ATsxuiQJ33RaO5Q%3A2%3A1711803443%3A-1%3A6200%3A%3AAcXnu0Ap22qYKWWCiLTVhDu1BmdLALCh3gwFDcT78jQ; fr=1uAMLlGoLkolg8srK.AWXTOILHsvwOvZ9EWTGt9G1TYt8.BmG6ZY..AAA.0.0.BmG6ZY.AWWL7t-RxTI; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1713088090202%2C%22v%22%3A1%7D; m_page_voice=100007681321904"
LINK_OR_UID_OR_USERNAME = "https://mbasic.facebook.com/thithanh.bui.58173000/friends?lst=100007681321904%3A100033728418502%3A1713112925&eav=Afaqo8BsThpyUkgln0qpg3R-nz-9kPCSQsarSmwTHPOzk3-KfeRk3rLwTde1JZWPvog&refid=17&paipv=0"
uid = get_uid_from_url(LINK_OR_UID_OR_USERNAME)
s = Session()


def get_friends_from_uid(s: Session, uid) -> list[dict]:
    friends = []
    r = s.get(BASE_URL / uid / "friends", cookies=string_to_dict(COOKIE))
    # if "No friends to show" in r.text:
    #     return friends
    while True:
        print('ahihi')
        with open('a.html', 'w', encoding='utf-8') as file:
            file.write(r.text)
        friends.extend(get_friends_from_html(r.text))
        urls = query_xpath(r.text, '//div[@id="m_more_friends"]/a/@href')
        if not urls:
            break
        r = s.get('https://mbasic.facebook.com' + urls[0], cookies=string_to_dict(COOKIE))
    return friends

def get_friends_from_html(html: str):
    friends = []
    elem_friends = query_xpath(html, XPATH_URL_FRIENDS)
    for elem in elem_friends:
        uid = get_uid_from_url(elem.get("href"))
        friends.append({"uid": uid, "name": elem.text})
    return friends


def save_to_file(list_friends: list[dict]):
    line_friends = []
    for friend in list_friends:
        line_friends.append(f'{friend['uid']} | {friend['name']}')
    with open('friends.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(line_friends))

list_friends = get_friends_from_uid(s, uid)
save_to_file(list_friends)
