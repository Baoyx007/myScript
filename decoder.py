# -*- coding: utf-8 -*-
__author__ = 'PCPC'
import codecs


def encode_url_utf8(data):
    hex_data = codecs.encode(data, 'hex')
    ret = ''
    for i, v in enumerate(hex_data):
        if i % 2 == 0:
            ret += r'%'
        ret += v
    print(ret)


encode_url_utf8('58同城')
