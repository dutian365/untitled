#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pymongo

url = 'http://s.5173.com/dnf-0-0-0-0-bx1xiv-0-0-0-a-a-a-a-a-0-0-0-0.shtml'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

res = requests.get(url,headers=headers).text
soup = BeautifulSoup(res,'lxml')

lists = []

for i in soup.select('div.sin_pdlbox'):
    d = {}
    d['title'] = i.h2.text
    d['price'] = float(i.strong.text)
    d['game'] = i.select('ul.pdlist_info li')[3].a.text
    lists.append(d)

def savedb(lists):
    client = pymongo.MongoClient('127.0.0.1')
    db = client.game
    t = db.currency
    t.insert(lists)



# client = pymongo.MongoClient('127.0.0.1')
# db = client.game
# t = db.currency
# for i in t.find().sort('price'):
#     print(i)