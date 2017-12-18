"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2017/12/10 00:25
"""
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient

headers = {
    'x-devtools-emulate-network-conditions-client-id': "5f2fc4da-c727-43c0-aad4-37fce8e3ff39",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'dnt': "1",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
    'cookie': "__c=1501326829; lastCity=101020100; __g=-; __l=r=https%3A%2F%2Fwww.google.com.hk%2F&l=%2F; __a=38940428.1501326829..1501326829.20.1.20.20; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1501326839; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1502948718; __c=1501326829; lastCity=101020100; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1501326839; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1502954829; __l=r=https%3A%2F%2Fwww.google.com.hk%2F&l=%2F; __a=38940428.1501326829..1501326829.21.1.21.21",
    'cache-control': "no-cache",
    'postman-token': "76554687-c4df-0c17-7cc0-5bf3845c9831"
}
conn = MongoClient('127.0.0.1', 27017)
db = conn.iApp  # 连接mydb数据库，没有则自动创建


def init():
    items = db.jobs_php.find().sort('pid')
    for item in items:
        if 'detail' in item.keys(): # 在爬虫挂掉再此爬取时，跳过已爬取的行
            continue
        detail_url = "https://www.zhipin.com/job_detail/%s.html?ka=search_list_1" % item['pid']
        print(detail_url)
        html = requests.get(detail_url, headers=headers)
        if html.status_code != 200: # 爬的太快网站返回403，这时等待解封吧
            print('status_code is %d' % html.status_code)
            break
        soup = BeautifulSoup(html.text, "html.parser")
        job = soup.select(".job-sec .text")
        if len(job) < 1:
            continue
        item['detail'] = job[0].text.strip()  # 职位描述
        location = soup.select(".job-sec .job-location")
        item['location'] = location[0].text.strip()  # 工作地点
        item['updated_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 实时爬取时间
        res = save(item) # 保存数据
        print(res)
        time.sleep(40) # 停停停


# 保存数据到 MongoDB 中
def save(item):
    return db.jobs_php.update_one({"_id": item['_id']}, {"$set": item})


if __name__ == "__main__":
    init()