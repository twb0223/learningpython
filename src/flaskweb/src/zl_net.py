# 爬取智联 武汉地区 所有.net 相关的 职位信息
import requests
from bs4 import BeautifulSoup
import pandas


pos = []
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'sou.zhaopin.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

for p in range(1, 50):

    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%AD%A6%E6%B1%89&kw=C#&sm=0&p=' + \
        str(p)

    re = requests.get(url, headers=headers)
    bs = BeautifulSoup(re.text, 'lxml')

    tb = bs.find_all('table', class_="newlist")
    for x in tb:
        res = {}
        zw = x.find('td', class_="zwmc")
        if(zw):
            res["Posion"] = zw.find("a").text

        gs = x.find('td', class_="gsmc")
        if(gs):
            res["Company"] = gs.text

        xs = x.find('td', class_="zwyx")
        if(xs):
            res["Salary"] = xs.text

        if(len(res) > 0):
            pos.append(res)

pandas.DataFrame(pos).to_json('./src/flaskweb/zl_net.json', orient='records')
