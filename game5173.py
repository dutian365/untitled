#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pymongo
import re
import csv

def get_lists(url):
    url = url
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    res = requests.get(url,headers=headers).text
    soup = BeautifulSoup(res,'lxml')

    lists = []
    '''
    [<a href="http://danbao.5173.com/detail/DB061-20170625-67273399.shtml" onclick="_hmt.push(['_trackEvent', '搜寻列表页', '点击量', '担保订单','http://danbao.5173.com/detail/DB061-20170625-67273399.shtml']);" target="_blank">820000万金币 ＝ 500元 【在线发货，方便快捷】</a>,
    <a href="http://pingjia.5173.com/Appraise/CreditAppraise/ELIFmKQRhftlfOmHwKlt9GiNeVVjHRZK" target="_blank" title="一钻卖家（250-500个信用积分）"><span class="ico_dm_1"></span></a>,
    <a href="http://s.5173.com/dnf-0-0-0-0-bx1xiv-0-0-0-a-a-a-a-a-0-0-0-0.shtml" title="查看 地下城与勇士/游戏币 所有商品">游戏币</a>,
     <a href="http://s.5173.com/dnf-0-0-0-0-bx1xiv-0-0-0-a-a-a-a-a-0-0-0-0.shtml" title="查看 地下城与勇士 所有商品">地下城与勇士</a>,
     <a href="http://s.5173.com/dnf-0-mi3hwi-0-0-bx1xiv-0-0-0-a-a-a-a-a-0-0-0-0.shtml" title="查看 地下城与勇士/体验区 所有商品">体验区</a>,
     <a href="http://s.5173.com/dnf-0-mi3hwi-hvlbqn-0-bx1xiv-0-0-0-a-a-a-a-a-0-0-0-0.shtml" title="查看 地下城与勇士/体验区/体验3服 所有商品">体验3服</a>]

    '''
    for i in soup.select('div.sin_pdlbox'):
        d = {}
        d['商品名称'] = i.h2.text
        d['出售价格'] = float(i.strong.text)
        d['物品数量'] = re.split('＝|=',i.h2.text )[0]
        d['物品单价'] = i.select('ul.pdlist_unitprice li')[1].text
        d['游戏'] = i.select('ul.pdlist_info li')[3].a.text
        d['区服'] = i.select('ul.pdlist_info li a')[4].text
        d['发布描述'] = i.h2.text
        d['交易状态'] = ' '
        d['发布人'] = ' '
        lists.append(d)
    return lists

def savedb(lists):
    client = pymongo.MongoClient('127.0.0.1')
    db = client.game
    t = db.lists
    t.insert(lists)


def savecsv(lists):
    fn = lists[0]['游戏']+'.csv'
    with open(fn, 'w') as csvfile:
        fieldnames = ['游戏', '区服' ,'商品名称' ,'出售价格','交易状态' ,'物品数量','物品单价','发布人','发布描述']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in lists:
            writer.writerow(i)


savecsv(get_lists('http://s.5173.com/search/778488dfc5bb4ee1900020a664f22c09-0-0-0-0-wkqq21-0-0-0-a-a-a-a-a-0-0-0-0.shtml'))
#print(lists)
#savedb(lists)
# client = pymongo.MongoClient('127.0.0.1')
# db = client.game
# t = db.lists
# for i in t.find():
#     print(i)