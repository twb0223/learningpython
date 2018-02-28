from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import random

url = 'https://www.oschina.net/widgets/index_tweet_list'

headers = {
    'Accept':
    '*/*',
    'Accept-Encoding':
    'gzip, deflate, br',
    'Accept-Language':
    'zh-CN,zh;q=0.9',
    'Cache-Control':
    'no-cache',
    'Connection':
    'keep-alive',
    'Content-Length':
    '0',
    'Host':
    'www.oschina.net',
    'Origin':
    'https://www.oschina.net',
    'Pragma':
    'no-cache',
    'Referer':
    'https://www.oschina.net/',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'X-Requested-With':
    'XMLHttpRequest'
}

ip_list = []


def get_ip_list():
    global ip_list
    ipurl = 'http://www.xicidaili.com/nn/'
    header = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    ip_data = requests.get(ipurl, headers=header)

    soup = bs(ip_data.text, 'lxml')
    ips = soup.find_all('tr')

    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[i].text + ":" + tds[2].text)
    return ip_list


def get_random_ip(iplist):
    proxy_list = []
    for ip in iplist:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxyies = {'http': proxy_ip}
    return proxyies


def get_msg():
    web_data = requests.get(url, headers=headers)
    
    df = bs(web_data.text, 'lxml')
   # print(df.prettify())
    re = df.find_all('p', {'class': 'tweet-content wrap'})
    lst = []
    for p in re:
        href = p.find('a').get('href')
        autor = p.find('a').get('title')
        message = p.text
        if autor:
            res = {'autor': autor, 'href': href, 'message': message}
            lst.append(res)

    head = ["autor", "message", "href"]
    df = pd.DataFrame(lst, columns=head)
    print(df)


if __name__ == '__main__':
    get_msg()
    #print(get_ip_list())
