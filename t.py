#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import logging



logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('monitor.log')
fh.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)


url = 'http://www.qqgonglue.com/php/do12.php?url=http://t.cn/RcxXPw9'
#url = 'http://www.qqgonglue.com/php/do12.php?url=http://t.cn/RSKKOze'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'__cfduid=d2acd7011730d7a08d9502b7e3479b0861496822133; UM_distinctid=15c818d362a8d2-0b9d835f4360b9-396d7804-1fa400-15c818d362c8e6; bdshare_firstime=1496822134353; PHPSESSID=8kqui0d40bft18ecat5h4d9476; CNZZDATA1260063679=1384119271-1496822044-https%253A%252F%252Fwww.baidu.com%252F%7C1497938593; Hm_lvt_7315998b2390029b80ed93e1779211e2=1496822135,1497941636,1497941666; Hm_lpvt_7315998b2390029b80ed93e1779211e2=1497941666',
    'Host':'www.qqgonglue.com',
    'Referer':'http://www.qqgonglue.com/',
    'X-Requested-With':'XMLHttpRequest'
    }
s = requests.get(url,headers=headers).text

logger.info(s)
