from instagrapi import Client
from time import sleep
from typing import Dict, List
from random import *
#import sys
#import time

cl = Client()
username = 'toxics3d' 
password ='test12345678'
cl.login(username, password)

session_userid = cl.user_id_from_username(username)

followed = cl.user_info_by_username('toxics3d').dict()["following_count"]
new_followed = followed + 10 
media=1 
medias = cl.hashtag_medias_top('model', amount=media)

account_to_follow=[]

while followed < new_followed : 

    for i in range(0, len(medias)):
        user_to_follow = cl.user_id_from_username(medias[i].dict()["user"]["username"])
        user_followed = cl.user_followers(cl.user_id)

        for user_to_follow in user_followed.keys():
            cl.user_follow(user_to_follow)
    
    newmedia=media+1
      
        