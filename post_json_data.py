# -*- coding: utf-8 -*-
__author__ = 'PCPC'
import requests


def post_data():
    frame_ids = {"frameids": [72,33,38,44,45,108]}
    headers = {'Content-Type': 'application/json'}
    r = requests.post('http://127.0.0.1:8080/autogen_1/6', json=frame_ids, headers=headers)
    print(r.text)


post_data()
