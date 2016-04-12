# -*- coding: utf-8 -*-
import requests
import urllib.request
import urllib.parse

Login_url = 'http://10.9.27.18/include/auth_action.php'


def login():
    username = 'xx'
    password = 'xx'
    login_data = {"username": username, "password": password, "action": 'login', 'ajax': '1', 'ac_id': '4'}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36',
        'Host': "10.9.27.18",
        'Referer': 'http://10.9.27.18/srun_portal_pc.php?url=www.baidu.com&ac_id=4',
        'X-Requested-With': "XMLHttpRequest",
        'Origin': 'http://10.0.27.18',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4'
    }

    r = requests.post(Login_url, data=login_data, headers=header)
    print(r.text, r.status_code)


# login()
def login_without_requests():
    username = '51141500001'
    password = 'byx100200ecnu'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36',
        'Host': "10.9.27.18",
        'Referer': 'http://10.9.27.18/srun_portal_pc.php?url=www.baidu.com&ac_id=4',
        'X-Requested-With': "XMLHttpRequest",
        'Origin': 'http://10.0.27.18',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4'
    }
    login_data = {"username": username, "password": password, "action": 'login', 'ajax': '1', 'ac_id': '4'}
    # pdata为post内容,为dict类型
    tmp_pdata = urllib.parse.urlencode(login_data)
    req = urllib.request.Request(url=Login_url, \
                                 data=tmp_pdata.encode(encoding="utf-8", errors="ignore"), \
                                 headers=header, method='POST')

    with urllib.request.urlopen(req, timeout=120) as f:
        print(f.read(300))


login_without_requests()
