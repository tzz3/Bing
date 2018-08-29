import requests
import json
import pymysql
import urllib.request
import os

bingUrl = 'https://cn.bing.com/'
idx = 0  # 日期标志
apiUrl = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=' + str(idx) + '&n=1&nc=1535091917942&pid=hp'
r = requests.get(apiUrl)  # 获取到json
r = json.loads(r.text)  # 转化为dict类型

imageUrl = bingUrl + r['images'][0]['url']

print(apiUrl)
# print(imageUrl)

supPath = os.path.dirname(os.path.dirname(__file__))  # 获取上级路径
relPath = os.path.relpath(supPath, os.getcwd())  # 相对路径

path = os.path.join(relPath, 'images')

if not os.path.exists(path) or os.path.isfile(path):
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
