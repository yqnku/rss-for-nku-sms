#!/usr/bin/python3
# -*- coding: <utf-8> -*-

#************************************************************************
# File Name: rss.py
# Author: quicy
# Email: xiqian013@live.com 
# Created Time: 2016-07-27 22:13:30
#************************************************************************

import requests
import re
import xml.etree.ElementTree as ET
from traceback import format_tb
import time
import sys
sys.path.append("..")
from config.config import *


#测试网络是否可用,并判断是否是502页面
def testNet():
    try:
        conn = requests.get(URL)
        content = conn.text
        if (content.find('502 Bad Gateway') != -1):
            return False
        return True
    except:
        return False

#获取页面上的名称，超链接和时间内容
def getContent(page):
    result = RESULT_RE.findall(page)
    return result

#将获取到的内容放到一个表里
def getContentTable():
    table = []
    for link in LINKS:
        try:
            conn = requests.get(URL + link)
            content = conn.text 
            table.append(getContent(content))
        except Exception as exc:
            print(format_tb(exc.__traceback__)[0])
    return table

#获取网页上最新的内容
def getNowLatest(table):
    nowLatests = []
    for c in table:
        nowLatests.append(c[0][0])
    return nowLatests

#获得本地上最新的内容
def getLocalLatest():
    localLatest = open(LATEST_FILE_PATH,'r')
    localLatests = localLatest.readlines()
    localLatest.close()
    return localLatests

#判断是否有更新
def isUpdated(table,local):
    nowLatests = getNowLatest(table)
    localLatests = local
    for i in range(len(nowLatests)):
        if (nowLatests[i].strip() + '\n') != localLatests[i]:
            return False;
    return True;

#获得具体的更新
def getUpdate(table,local):
    result = [] 
    length = len(table)
    for i in range(length):
        l = []
        c = table[i]
        j = 0
        maxLength = len(c)
        while (j < maxLength) and (c[j][0]+'\n' != local[i]):
            l.append(c[j]) 
            j = j + 1
        l.reverse()
        result.append(l)
    return result

#新建一个elem节点:
def createElem(title,link,date):
    element_item = ET.Element('item')
    element_title = ET.Element('title')
    element_link = ET.Element('link')
    element_description = ET.Element('description')
    element_date = ET.Element('date')
    element_title.text = title
    element_link.text = link
    element_description.text = title
    element_date.text = date
    element_item.insert(0,element_date)
    element_item.insert(0,element_description)
    element_item.insert(0,element_link)
    element_item.insert(0,element_title)
    return element_item

#更新XML文件
def updateXML(table,local):
    files = ['xyxw.xml','bksjw.xml','yjsjw.xml','kydt.xml','xsgz.xml','ggsx.xml']
    files = [RSS_PATH+i for i in files]
    length = len(files)
    update = getUpdate(table,local)
    for i in range(length):
        tree = ET.parse(files[i])
        root = tree.getroot()
        channel = root.getchildren()[0]
        if update[i] != []:
            for item in update[i]:
                channel.insert(3,createElem(item[1],URL + item[0],item[2]))
        tree.write(files[i])

#更新latest文件
def updateLatest(table):
    f = open(LATEST_FILE_PATH,'w')
    latest = getNowLatest(table)
    for l in latest:
        f.write(l+'\n')
    f.close()

if __name__ == '__main__':
    print("\n######################################")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    if (testNet()):
        table = getContentTable()
        local = getLocalLatest()
        if not isUpdated(table,local):
            updateXML(table,local)
            updateLatest(table)
            update = getUpdate(table,local)
            print(update)
            print("updated!")
        else:
            print("no update!")
    else:
        print("网络连接失败")
    print("######################################\n")
