from instagrapi import Client
from time import sleep
from typing import Dict, List
from random import *
import pickle
import json
#import sys
#import time

cl = Client()
username = 't0ixcsed' 
password ='test12345678'
cl.login(username, password)

media_count = cl.user_info_by_username_gql('weiefrei').dict()["media_count"]

print(media_count)


media = cl.user_medias_gql(cl.user_id_from_username('weiefrei') , 1, )


print(media)
with open('media.json', 'wb') as temp:
    print(json.dumps(media))
