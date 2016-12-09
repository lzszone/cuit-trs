#coding=utf-8

import module.MailService
import os
import threading
import urllib.request as Request
import datetime
import time

#这个脚本用来从https://forcuit-151103.appspot.com/news_xueshu_update 获取我们学校学术预告的更新新闻的


print("\t\t|->CUIT Auto News Retriver started!")
now = datetime.datetime.now()
timestr = now.strftime('%Y-%m-%d %H:%M:%S')  
print("\t\t|->CUIT->start check news update...")
url = "https://forcuit-151103.appspot.com/news_xueshu_update"
page = Request.urlopen(url)
data = page.read().decode("utf-8","igonre")
if data=="NO UPDATE YET":
    print("\t\t|->\tCUIT:XueshuNews->no update yet")
else:
    updatelist = data.split("<br/>")
    newscontent = ""
    for news in updatelist:
        if len(news) < 5:
            continue
        news = news.split("<@>")
        href = "\t<p><a href=\"" + news[2] + "\"target=\"_blank\">" + news[1] + news[0] + "</a></p>"
        newscontent+=href
    data = "有新的学术预告！\r\n\r\n" + newscontent + "\r\n\r\n\r\n**你之所以会收到该邮件，是因为你已经订阅成都信息工程大学学术预告新闻更新。"
    MailService.SendMail("1075900121@qq.com","成都信息工程大学->新【学术预告】",data)
    print("\t\t|->CUIT:XueshuNews->news update!")
    Request.urlopen("https://forcuit-151103.appspot.com/news_xueshu").read()