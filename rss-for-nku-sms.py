#!/usr/bin/python3
# -*- coding: <utf-8> -*-

#************************************************************************
# File Name: RssForSMS.py
# Author: yqnku
# Mail: xiqian013@live.com 
# Created Time: 2016-01-22 15:48:38
#************************************************************************

import smtplib, email
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import http.client
import re

def _format_addr(s):
    (name, addr) = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr))
     
def SendMail(contents,to_addr):
    ###########################################################
    from_addr = ''
    from_name = ''
    password = ''
    to_name = ''
    smtp_server = 'smtp.163.com'
    heading = 'RSS For SMS'
    ###########################################################
    main_body = contents
    from_attr = from_name + ' < ' + from_addr + ' > '
    to_attr = to_name + ' < ' + to_addr + ' > '

    msg = MIMEText(main_body, 'html', 'utf-8')
    msg['From'] = _format_addr(from_attr)
    msg['To'] = _format_addr(to_attr)
    msg['Subject'] = Header(heading, 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.connect(smtp_server, 25)
    server.helo()
    server.ehlo()
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

def GetTitleAndLinks(url):
    conn = http.client.HTTPConnection("sms.nankai.edu.cn")
    conn.request("GET",url)
    res = conn.getresponse()
    page = res.read().decode("utf-8")
    r = re.compile('<a target="_blank" href="(.*?)">(.*?)</a>')
    return r.findall(page)

def GetLoaclLatest():
    #latest.txt
    #Line1----http://sms.nankai.edu.cn/html/bksjx/all
    #line2----http://sms.nankai.edu.cn/html/xsgz/all
    f = open(r'latest.txt','r')
    tmp = (f.readline()[:-1],f.readline()[:-1])
    f.close()
    return tmp

def GetWebLatest(page1,page2):
    return (page1[0][0].strip(),page2[0][0].strip())

def IsUpdated(page1,page2):
    return GetWebLatest(page1,page2) == GetLoaclLatest()

def UpdateLatest(page1,page2):
    f = open(r'latest.txt','w')
    WebLatest = GetWebLatest(page1,page2)
    f.write(WebLatest[0]+"\n")
    f.write(WebLatest[1]+"\n")

def GetNew(page1,page2):
    LocalLatest = GetLoaclLatest()
    message = '<html><h3>New news For NKU School of Mathematical and Science</h3>'
    for i in range(len(page1)):
        if (page1[i][0] == LocalLatest[0]):
            break
        else:
            message += '<a href = "http://sms.nankai.edu.cn'+page1[i][0]+'">'+page1[i][1]+'</a><br/>'
    for i in range(len(page2)):
        if (page2[i][0] == LocalLatest[1]):
            break
        else:
            message += '<a href = "http://sms.nankai.edu.cn'+page2[i][0]+'">'+page2[i][1]+'</a><br/>'
    message += 'Thanks For Using<br/></html>'
    return message

if __name__ == '__main__':
    page1 = GetTitleAndLinks('/html/bksjx/all')
    page2 = GetTitleAndLinks('/html/xsgz/all')
    if (IsUpdated(page1,page2)):
        print("no update")
    else:
        print("update!")
        new = GetNew(page1,page2)
        ##################################################
        SendMail(new,"")
        ##################################################
        UpdateLatest(page1,page2)

