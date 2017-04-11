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
import sys
sys.path.append("..")
from config.config import *


#发送微博
def sendsweibo(messages):
    c = Client(api_key,api_secret,redirect_url,username=name,password=pwd)
    for message in messages:
        c.post("statuses/update",status = message)
        time.sleep(5)

