# coding=utf-8
__author__ = "tzz6"

import requests
import json
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

    imageUrl = bingUrl + url  # 图片链接

    # print(imageUrl)

    image_dir_path = "bing/static/bing/images"
    rel_path = "bing/images"

    if not os.path.exists(image_dir_path) or os.path.isfile(image_dir_path):  # 判断文件夹是否存在
        os.makedirs(image_dir_path)

    save_path = os.path.join(image_dir_path, imageUrl.split('/')[-1])  # 保存文件地址
    path = os.path.join(rel_path, imageUrl.split('/')[-1])

    def schedule(a, b, c):  # 下载进度
        per = 100.0 * a * b / c
        if per > 100:
            per = 100
        print('%.2f %%' % per)

    # E:\Workspaces\djangoBing\bing\images
    if not os.path.exists(save_path):  # 判断图片是否已存在
        urllib.request.urlretrieve(imageUrl, save_path, schedule)
    else:
        print("have saved")

    conn = sqlite3.connect("../../db.sqlite3")
    c = conn.cursor()

    insert_sql = "INSERT INTO bing_images (startdate, fullstartdate, enddate, url, urlbase, copyright, copyrightlink, title, quiz, hsh, path) " \
                 "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                 % (startdate, fullstartdate, enddate, url, urlbase, copyright, copyrightlink, title, quiz, hsh, path)
    print(insert_sql)
    r = c.execute("select * from bing_images where startdate = " + startdate)
    if not r.fetchone():
        c.execute(insert_sql)
        conn.commit()
        print(enddate, " 插入完成")
    else:
        print(enddate, " 已存在")
    result = c.execute("select * from bing_images")
    # for r in result:
    #     for l in range(len(r)):
    #         print(r[l], end="\n")
    c.close()


if __name__ == '__main__':
    get_pic_from_bing()
