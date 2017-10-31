# coding=utf-8

import urllib
import urllib.request
import re


def download_page(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    data = data.decode('GBK')
    return data


def get_image(html):
    reg = r'src="(http.+?\.jpg)"'

    pattern = re.compile(reg)
    get_img = re.findall(pattern, html)
    num = 0
    for img in get_img:
        urllib.request.urlretrieve(img, 'D:\picture\%s.jpg' % num)
        num += 1
        print('正在下载第%s张照片' % num)
    return get_img

html = download_page("http://www.metarthunter.com/most-viewed/")
get_image(html)
