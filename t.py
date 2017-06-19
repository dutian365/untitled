#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ------------zhuanke8_spider.py-----------------
# -*- coding: utf-8 -*-
from pyquery import PyQuery as py
from datetime import datetime
from requests.exceptions import ConnectionError
import io
import sys
import time
import os
import re
import logging
import configparser

# 全局变量
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
logging.basicConfig(level=logging.INFO)
config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath('.'), 'zhuanke8_spider_config.ini'), encoding='utf-8')
headers = {'User-Agent': config.get('config', 'User-Agent')}
keyword = config.get('config', 'keyword')
exceptword = config.get('config', 'exceptword')
fileName = config.get('config', 'fileName')
interval = int(config.get('disable', 'interval'))
maxcount = int(config.get('disable', 'maxcount'))
encoding = config.get('disable', 'encoding')
pushDict = dict()
newDict = dict()


def dealPost(i, e):
    now = datetime.now().timestamp()
    postId = str(py(e).attr('id'))
    if not re.match('normalthread', postId):
        return
    # 已存在
    if pushDict.get(postId):
        return
    title = py(e).find('th').text()  # 帖子标题
    if not re.match(r'.*(' + keyword + ').*', title) or re.match(r'.*' + exceptword + '.*', title):
        return
    url = py(e).find('th a').attr('href')  # 帖子地址
    byElement = py(e).find('td:eq(1)')  # class="by"
    postTimeStamp = datetime.strptime(byElement.find('em').text(), '%Y-%m-%d %H:%M').timestamp()
    if now - postTimeStamp < 5 * 60:
        content = dealPostUrl(url)
        newDict[postId] = {'url': url, 'title': title, 'time': byElement.find('em').text(), 'content': content}
        pushDict[postId] = {'url': url, 'title': title, 'time': byElement.find('em').text(), 'content': content}


def dealPostUrl(url):
    d = py(url, headers=headers, encoding=encoding)
    div = d('#postlist>div:first')
    tr = div.find('tr:first')
    content = tr.find('.t_f').text()
    return content


if __name__ == '__main__':
    logging.info('正在运行！')
    logging.info('动态内容，请查看当前目录：' + fileName + "！")
    count = 0
    url = 'http://www.zuanke8.com/forum.php?mod=forumdisplay&fid=15&filter=author&orderby=dateline'
    while True:
        try:
            d = py(url, headers=headers, encoding=encoding)
            d('#threadlisttableid tbody').each(dealPost)
        except ConnectionError:
            logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' 发生点网络小异常！')
            continue

        # 输出推送内容
        with open(os.path.join(os.path.abspath('.'), fileName), 'a', encoding='utf-8') as file:
            for key, value in newDict.items():
                result = '发帖时间：' + value['time'] + '\n标题：' + value['title'] + '\n内容：' + value['content'] + '\n'
                logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n' + result)
                file.write(result + '\n')
        newDict.clear()
        time.sleep(interval)
        count += 1
        # 5分钟后重置
        if count == 10:
            pushDict.clear()
            count = 0

    logging.info('运行结束！')


