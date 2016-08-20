#!/usr/bin/python3
# -*- coding: <utf-8> -*-

#************************************************************************
# File Name: sendweibo.py
# Author: quicy
# Email: xiqian013@live.com 
# Created Time: 2016-08-04 13:51:41
#************************************************************************

from weibo import Client
import time

api_key = #你的应用Key
api_secret = #你的应用Secret
redirect_url = #你的应用回调地址
name = #你的微博用户名
pwd = #你的微博密码

#发送微博
def sendsweibo(messages):
    c = Client(api_key,api_secret,redirect_url,username=name,password=pwd)
    for message in messages:
        c.post("statuses/update",status = message)
        time.sleep(5)

