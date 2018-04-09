from flask import Flask, send_file, request,render_template,jsonify
import json
import pandas
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def crawdata(type):
    pos = []
    headers = {
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':
        'gzip, deflate',
        'Accept-Language':
        'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection':
        'keep-alive',
        'Host':
        'sou.zhaopin.com',
        'Upgrade-Insecure-Requests':
        '1',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }
    url = ''
    if (type is '1'):
        url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%AD%A6%E6%B1%89&kw=python&sm=0&p='
    else:
        url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%AD%A6%E6%B1%89&kw=.net&sm=0&p='

    for p in range(1, 20):

        url = url + str(p)

        re = requests.get(url, headers=headers)
        bs = BeautifulSoup(re.text, 'lxml')

        tb = bs.find_all('table', class_="newlist")
        for x in tb:
            res = {}
            zw = x.find('td', class_="zwmc")
            if (zw):
                res["职位"] = zw.find("a").text

            gs = x.find('td', class_="gsmc")
            if (gs):
                res["公司名称"] = gs.text

            xs = x.find('td', class_="zwyx")
            if (xs):
                res["工资"] = xs.text

            if (len(res) > 0):
                pos.append(res)
    return pos
    #pandas.DataFrame(pos).to_json('zl_python.json',orient='records')


@app.route('/')
def index():
    return send_file("templates\index.html")


@app.route('/get_json')
def getdata():
    text = request.args.get('type')
    res = []
    df = []
    if (text is '1'):
        df = pandas.read_json('./src/flaskweb/zl_python.json', encoding='utf-8')
    elif (text is '2'):
        df = pandas.read_json('./src/flaskweb/zl_net.json', encoding='utf-8')      
    else:
        df = pandas.read_json('./src/flaskweb/zl_java.json', encoding='utf-8')

    res = df.to_json(orient='records', force_ascii=False)
    return res

@app.route('/get_json2',methods=['POST'])
def getdata2():
    datax = request.form['Code']
    print(datax)
    return jsonify({'Name': 'AAA','Code':'AXXX','DispName':'SDWW_WQ'} , {'Name': 'BBB','Code':'BXXX','DispName':'SDWW_WQ'},{'Name': 'AA11A','Code':'AXX11X','DispName':'SDWW_WQ'})
 

def main():
    pass


if __name__ == '__main__':
    app.run()
