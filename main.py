import requests
import json
import glob
import random
import urllib
import time
import vk_api
import randomD
import os
import zalgo
import to_leet
from translate import Translator
import re


token = 'x'
group_id = 195384741
album_id = 272636969

def write_json(data,filename):
    with open(filename, 'w') as file:
        json.dump(data,file,indent = 2,ensure_ascii=False)

def get_upload_serv():
    r = requests.get('https://api.vk.com/method/photos.getUploadServer', params={'access_token' : token,
                                                                                 'album_id' : album_id,
                                                                                 'group_id' : group_id,
                                                                                 'v' : 5.103}).json()
    return r['response']['upload_url']


def main():
    while True:
        gg = randomD.main(1,'downloaded_imgurs')
        upload_url = get_upload_serv()
        to_dir = 'downloaded_imgurs/' + gg
        file = {'file': open(to_dir, 'rb')}
        ur = requests.post(upload_url,files=file).json()
        result = requests.post('https://api.vk.com/method/photos.save', params={
            'access_token':token,
            'album_id':ur['aid'],
            'group_id' :ur['gid'],
            'server' : ur['server'],
            'photos_list' : ur['photos_list'],
            'hash' : ur['hash'],
            'v' : 5.103}).json()
        ggz = result['response']
        ggz = str(ggz)
        ggz = ggz.split(',')
        ggz = ggz[2]
        ggz = ggz[7:9999]
        fr_post = 'photo-195384741_' + str(ggz)
        vk_session = vk_api.VkApi('d', 'd')
        vk_session.auth()
        vk = vk_session.get_api()
        random_stringg = '%^*&#@;№"~`'
        rrs = random.choice(random_stringg) + random.choice(random_stringg) + random.choice(random_stringg) + random.choice(random_stringg) * 2
        print(fr_post)
        f = open("ca_full.txt", "r")
        f = f.read()
        f = f.split(' ')

        rz = random.randint(1,4000)
        dd = re.sub(r'\d', '', f[rz])

        leet = to_leet.leet_decoration(dd)
        zalgo = zalgo.zalgo().zalgofy(leet)
        print(vk.wall.post(owner_id=-195384741,message = zalgo,attachments=fr_post,from_group=1))

        time.sleep(3600)
main()
