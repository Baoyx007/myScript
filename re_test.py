# -*- coding: utf-8 -*-
__author__ = 'PCPC'
import re

str = '''
<div class="ui raised segment" id="38"><p>id=38<br>HTTP/1.1&nbsp;200&nbsp;OK
<br/>Cache-Control:&nbsp;max-age=86400
<br/>Content-Length:&nbsp;284
<br/>Content-Type:&nbsp;text/plain
<br/>Date:&nbsp;Fri,&nbsp;08&nbsp;May&nbsp;2015&nbsp;02:51:01&nbsp;GMT
<br/>Expires:&nbsp;Sat,&nbsp;09&nbsp;May&nbsp;2015&nbsp;02:51:01&nbsp;GMT
<br/>Http_x_bd_logid:&nbsp;786649265
<br/>Http_x_bd_logid64:&nbsp;16558996061297821993
<br/>Server:&nbsp;apache
<br/>
<br/>{"content":{"addr":"上海市,上海市,普陀区,共青路,,289,中国,0","bldg":"","clf":"121.403753|31.227739|2000.000000","floor":"","indoor":"40","point":{"x":"121.403368","y":"31.228084"},"radius":"67.625394","ssid":"2047"},"result":{"error":"161","time":"2015-05-08&nbsp;10:51:01"}}</p></div>
'''

flag = re.search('31\.', str)

print(flag)
