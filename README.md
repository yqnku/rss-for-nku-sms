# rss-for-nku-sms

## 注意

在不久前因为服务器出现了一些问题导致RSS服务停止，最近会更新一下代码，之前忘了备份真的是QAQ

## 介绍

南开数院非官方RSS

## 功能

[南开数院](http://sms.nankai.edu.cn) 主页上会发布各种信息，但更新频率很低，手动刷新比较繁琐并收益很少。于是出现了这非官方RSS，在数院网站内容更新的五分钟内推送新内容至[南开大学数学科学学院](http://weibo.com/u/5627139429)非官方微博，同时发送邮件。订阅RSS的用户可以在RSS阅读器中进行更新。

## 订阅

[学院新闻](http://120.27.29.76/rss/nku_math/xyxw.xml) 

[本科生教育](http://120.27.29.76/rss/nku_math/bksjw.xml) 

[研究生教育](http://120.27.29.76/rss/nku_math/yjsjw.xml) 

[科研动态](http://120.27.29.76/rss/nku_math/kydt.xml) 

[学生工作](http://120.27.29.76/rss/nku_math/xsgz.xml) 

[公共数学](http://120.27.29.76/rss/nku_math/ggsx.xml) 

## 代码

公开所有源代码，用户名密码路径等部分请替换为自己的用户名密码路径，python版本为3.4.3，可能需要安装模块requests

## 原理

### *.xml

分类别存储数院消息，用于rss阅读器更新

### latest

在本地保存最新的新闻

### receivers

在本地保存邮件收件人

### rss.py

在数院官网抓取数据并写入*.xml文件及latest文件

### mail.py

发送邮件的接口

### weibo.py

新浪非官方API

### sendweibo.py

发送微博的接口

### main.py

主程序，数院新闻有更新时同步更新xml文件，发送微博及邮件

服务器在后台每五分钟会爬取一次数院官网的新闻，所以新闻延迟会在5分钟之内

## 更新

最后更新于2016.8.20

欢迎制作其他学院的版本
