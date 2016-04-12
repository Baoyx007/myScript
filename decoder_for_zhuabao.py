# -*- coding:utf-8 -*-
__author__ = 'haven'
import re
import codecs


def url_utf8(str):
    pass


def utf16(str, only=False):
    # if only:
    #     return codecs.unicode_escape_decode(str)
    p = re.compile(r'\\u([\w]{4})')
    return p.sub(lambda match: codecs.decode(match.group(), encoding='utf16'), str)


if __name__ == '__main__':
    str_utf16 = '{"errno":0,"cityid":4,"city":"\u4e0a\u6d77","result":[{"displayname":"\u534e\u4e1c\u5e08\u8303\u5927\u5b66\u5b66\u751f\u516c\u5bd3","address":"\u91d1\u6c99\u6c5f\u8def\u5357","lng":121.39803076013,"lat":31.235354145395,"cotype":2,"srctag":"penguinrgeo","oldaddr":"\u666e\u9640\u533a\u4e2d\u6c5f\u8def629\u53f7","score":"0","click":"2"},{"displayname":"\u5927\u6e21\u6cb3\u8def\u5730\u94c1\u7ad9","address":"\u666e\u9640\u533a\u5927\u6e21\u6cb3\u8def\u5730\u94c1\u7ad9","lng":121.40106531201,"lat":31.237639500538,"cotype":2,"srctag":"penguinrgeo"},{"displayname":"\u6d01\u5bb6\u5bbe\u9986","address":"\u666e\u9640\u533a\u4e2d\u6c5f\u8def669\u53f7","lng":121.39805369884,"lat":31.236011393003,"cotype":2,"srctag":"penguinrgeo"},{"displayname":"\u4e0a\u6d77\u79cb\u6797\u9601\u9152\u5e97(\u4e2d\u6c5f\u5e97)","address":"\u666e\u9640\u533a\u4e2d\u6c5f\u8def629\u53f79\u53f7","lng":121.39850243262,"lat":31.235625319619,"cotype":2,"srctag":"penguinrgeo"},{"displayname":"\u4e2d\u6c5f\u5c0f\u533a","address":"\u666e\u9640\u533a\u4e2d\u6c5f\u8def650\u5f04","lng":121.39874572683,"lat":31.235971059111,"cotype":2,"srctag":"penguinrgeo"},{"displayname":"\u534e\u4e1c\u5e08\u8303\u5927\u5b66\u5b66\u751f\u516c\u5bd3(\u4e1c\u95e8)","address":"\u666e\u9640\u533a\u4e2d\u6c5f\u8def629\u53f7","lng":121.39859316859,"lat":31.235420335271,"cotype":2,"srctag":"penguinrgeo"},{"displayname":"\u534e\u5e08\u5927\u827e\u9a91\u9a7e\u6821","address":"\u666e\u9640\u533a\u91d1\u6c99\u6c5f\u8def995\u53f7","lng":121.39685085649,"lat":31.236762014341,"cotype":2,"srctag":"penguinrgeo"},{"displayname":"\u4e2d\u6c5f\u5c0f\u533a(\u897f\u95e8)","address":"\u666e\u9640\u533a\u4e2d\u6c5f\u8def650\u5f04-1-58\u53f7","lng":121.39887534367,"lat":31.235383538049,"cotype":2,"srctag":"penguinrgeo"},{"displayname":"\u7533\u6c49\u5c0f\u533a","address":"\u666e\u9640\u533a\u91d1\u6c99\u6c5f\u8def1060\u53f7","lng":121.39782526927,"lat":31.237251934515,"cotype":2,"srctag":"penguinrgeo"},{"displayname":"\u7533\u6c49\u5927\u53a6","address":"\u666e\u9640\u533a\u4e2d\u6c5f\u8def839\u53f7","lng":121.3979539013,"lat":31.237433301317,"cotype":2,"srctag":"penguinrgeo"},{"displayname":"\u534e\u4e1c\u5e08\u5927\u4e09\u6751","address":"\u666e\u9640\u533a\u91d1\u6c99\u6c5f\u8def895\u5f041-69\u53f7","lng":121.39946057502,"lat":31.23639538266,"cotype":2,"srctag":"penguinrgeo"},{"displayname":"\u7533\u6c49\u5c0f\u533a(\u5357\u95e8)","address":"\u666e\u9640\u533a\u91d1\u6c99\u6c5f\u8def1060\u53f7","lng":121.39795387526,"lat":31.237703294489,"cotype":2,"srctag":"penguinrgeo"},{"displayname":"\u534e\u4e1c\u5e08\u8303\u5927\u5b66\u540c\u666e\u8def\u7814\u7a76\u751f\u516c\u5bd3","address":"\u666e\u9640\u533a\u540c\u666e\u8def158\u5f041~14\u53f7","lng":121.39925517515,"lat":31.234585942985,"cotype":2,"srctag":"penguinrgeo"},{"displayname":"\u5929\u5730\u8f6f\u4ef6\u56ed","address":"\u666e\u9640\u533a\u4e2d\u6c5f\u8def879\u53f7","lng":121.39675999472,"lat":31.237838107395,"cotype":2,"srctag":"penguinrgeo"},{"displayname":"\u7533\u6c49\u5c0f\u533a(\u4e1c\u95e8)","address":"\u666e\u9640\u533a\u4e2d\u6c5f\u8def718\u9644\u8fd1","lng":121.3985551212,"lat":31.238209868464,"cotype":2,"srctag":"penguinrgeo"}],"is_wanliu":1,"city_open":1,"project_info":{"open":-1,"fast_car":{"open":0,"bill_ability":0,"msg":"\u5f53\u524d\u57ce\u5e02\u5c1a\u672a\u5f00\u901a\u5feb\u8f66,\u656c\u8bf7\u671f\u5f85","enter_name":"\u5feb\u8f66"},"topic_car":{"open":-1}},"guankong":0,"cityname":"\u4e0a\u6d77","lng":"121.397766","lat":"31.236012","tip":[],"new_guankong":0}'
    print(str_utf16, type(str_utf16))
    print(utf16(str_utf16))
