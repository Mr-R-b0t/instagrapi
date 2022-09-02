from doctest import testsource
from instagrapi import Client
from time import sleep
from typing import Dict, List
from random import *
import sys
import time

cl = Client()
cl.login('toxicsed@gmail.com', 'test12345678')

medias = cl.user_info_by_username('toxics3d')
test= medias.dict()["following_count"]
print(test)

medias = cl.hashtag_medias_top('downhill', amount=2)
medias[0].dict()
