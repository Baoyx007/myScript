# -*- coding:utf-8 -*-

__author__ = 'haven'

import requests

url='https://api.weibo.com/2/statuses/public_timeline.json'
url_loc = 'https://api.weibo.com/2/common/code_to_location.json'
res = requests.get(url_loc,params={'codes':'100'})
print(res.text)