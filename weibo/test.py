# -*- coding: utf-8 -*-
__author__ = 'PCPC'
import requests

app_key = '717625460'
app_secret = '95d69b729b8b89fbff4db9bb0671f163'
url = 'https://api.weibo.com/2/common/code_to_location.json'
res = requests.get(url,params={'codes':100,'source':app_key})
print(res.text)
