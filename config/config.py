#!/usr/bin/python3
# -*- coding: <utf-8> -*-

#************************************************************************
# File Name: config.py
# Author: quicy
# Email: xiqian013@live.com 
# Created Time: 2017-04-11 09:53:11
#************************************************************************


#config

import os
import re
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

URL = 'http://sms.nankai.edu.cn'
LINKS = [
    '/5547/list.htm', #学院新闻
    '/5536/list.htm', #本科生教育
    '/5537/list.htm', #研究生教育
    '/5538/list.htm',  #科研动态
    '/5540/list.htm',  #学生工作
    '/5539/list.htm',  #公共数学
]
RESULT_RE = re.compile("<li><a href='(.+?)' target='_blank' title='(.+?)'>(.+?)</a><span>(.+?)</span></li>")

#本地更新保存地址
LATEST_FILE_PATH = os.path.join(BASE_DIR,'config')

#rss保存地址
RSS_PATH = os.path.join(BASE_DIR,'rss')

##邮件
#你的电子邮件地址
From = ""
#你的密码
pwd = ""
#SMTP地址
smtp_server = ""
#端口
port = ""
#你的收件人文件地址
ReceiverPath = ""



##微博
#你的应用Key
api_key = ""
#你的应用Secret
api_secret = ""
#你的应用回调地址
redirect_url = "" 
#你的微博用户名
name = ""
#你的微博密码
pwd = ""

