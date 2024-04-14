import os
import requests
from lxml import html
#  get link song
r = requests.get('https://nhac.vn/bang-xep-hang-bai-hat-viet-nam-bxdE')
# write to file to checking
with open('nhac.html', 'w', encoding='utf-8') as file:
    file.write(r.text)
# search in file html by xpath
tree = html.fromstring(r.text.encode())
id_song_str_list = tree.xpath('''//ul[contains(@class, 'bxh_song_list')]/li/@id''')
newpath = 'song' 
if not os.path.exists(newpath):
    os.makedirs(newpath)
for id_song in id_song_str_list:
    id = id_song.split('song_')
    headers = {
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'id': id[1],
        'pid': '1'
    }
    r = requests.post('https://nhac.vn/ajax/getProfileSongDownloadV2', data=data, headers=headers)
    link_down_song = r.json()['errorMsg']
    r = requests.get(link_down_song)
    name_file = link_down_song.split('title=')[1]
    with open('song\\' + name_file, 'wb') as file:
        file.write(r.content)