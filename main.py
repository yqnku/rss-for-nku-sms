#!/usr/bin/python3
# -*- coding: <utf-8> -*-

#************************************************************************
# File Name: main.py
# Author: quicy
# Email: xiqian013@live.com 
# Created Time: 2016-08-08 15:07:26
#************************************************************************

from code.rss import *
from code.mail import *
from code.sendweibo import *
from traceback import format_tb
from config.config import *


#构造邮件发送信息
def makeMessage(table,local):
    updates = getUpdate(table,local)
    message = "New news for NKU SMS\n"
    for update in updates:
        if update != []:
            update.reverse()
            for item in update:
                message += "Title:%s \nLink: http://sms.nankai.edu.cn%s \n" %(item[1],item[0])
    return message
    print(message)

#发送邮件
def sendMail(table,local):
    message = makeMessage(table,local)
    f = open(ReceiverPath,'r')
    receivers = f.readlines()
    receivers = [receivers[2*i+1][:-1] for i in range(int(len(receivers)/2))]
    print(receivers)
    f.close()
    sends(receivers,message)

#构造微博发送信息
def makeWeiboMessages(table,local):
    updates = getUpdate(table,local)
    messages = []
    for update in updates:
        if update != []:
            for item in update:
                message = "#南开数院新闻推送# %s http://sms.nankai.edu.cn%s" %(item[1],item[0])
                messages.append(message)
    return messages
    print(messages)

#发送微博
def sendWeibo(table,local):
    try:
        messages = makeWeiboMessages(table,local)
        print(messages)
        sendsweibo(messages)
    except Exception as exc:
        print(format_tb(exc.__traceback__)[0])

if __name__ == '__main__':
    try:
        print("\n######################################")
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        if (testNet()):
            table = getContentTable()
            local = getLocalLatest()
            if not isUpdated(table,local):
                updateXML(table,local)
                updateLatest(table)
                #sendWeibo(table,local)
                #sendMail(table,local)
                print("updated!")
            else:
                print("no update!")
        else:
            print("网络连接失败")
        print("######################################\n")
    except Exception as exc:
        print(format_tb(exc.__traceback__)[0])
