# coding=utf-8
__author__ = "tzz6"

import requests
import json
import pymysql
import urllib.request
import os
import sqlite3


def get_pic_from_bing():
    bingUrl = 'https://cn.bing.com/'
    idx = 0  # 日期标志
    apiUrl = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=' + str(idx) + '&n=1&nc=1535091917942&pid=hp'
    r = requests.get(apiUrl)  # 获取到json
    r = json.loads(r.text)  # 转化为dict类型

    images = r['images'][0]
    print(images)

    startdate = images['startdate']
    fullstartdate = images['fullstartdate']
    enddate = images['enddate']
    url = images['url']
    urlbase = images['urlbase']
    copyright = images['copyright']
    copyrightlink = images['copyrightlink']
    title = images['title']
    quiz = images['quiz']
    wp = images['wp']
    hsh = images['hsh']
    drk = images['drk']
    top = images['top']
    bot = images['bot']
    hs = images['hs']

    imageUrl = bingUrl + url  # 图片链接

    # print(imageUrl)

    supPath = os.path.dirname(os.path.dirname(__file__))  # 获取上级路径
    relPath = os.path.relpath(supPath, os.getcwd())  # 相对路径

    path = os.path.join(relPath, 'images')

    if not os.path.exists(path) or os.path.isfile(path):  # 判断文件夹是否存在
        os.makedirs(path)

    local = os.path.join(path, imageUrl.split('/')[-1])  # 保存文件地址

    def Schedule(a, b, c):  # 下载进度
        per = 100.0 * a * b / c
        if per > 100:
            per = 100
        print('%.2f %%' % per)

    if not os.path.exists(local):  # 判断图片是否已存在
        urllib.request.urlretrieve(imageUrl, local, Schedule)
    else:
        print("have saved")

    # 返回每个信息 在models里获取到再进行数据插入


if __name__ == '__main__':
    get_pic_from_bing()
    c = sqlite3.connect("../../db.sqlite3")
    c = c.cursor()

    insert_sql = "INSERT INTO bing_images (startdate, fullstartdate, enddate, url, urlbase, copyright, copyrightlink, title, quiz, hsh, drk, top, bot, hs, path) VALUES ()"
    result = c.execute("select * from bing_images")
    for r in result:
        for l in range(len(r)):
            print(r[l], end="\n")
