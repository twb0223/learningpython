from os import path

import jieba
import matplotlib.pyplot as plt
import numpy as np
import requests
from PIL import Image
from pyquery import PyQuery as pq
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

headers = {'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Connection': 'keep-alive',
           'Content-Length': '0',
           'Cookie': '_user_behavior_=20aa1126-015b-49a3-8368-da720368470b; oscid=HPb1NGcm6pUtJvfY9J6PpNFZPGeaXecn%2FFzIdOALIoreGcwTUq4EMU2SyImcBbZJbCNUpMjdwmDk70OrzuzwE0huLwYMoT%2FcNKrH8M2O8rIM9sMwAAi0jBtzvkGMLGKfJfkvfNU0%2FioBI2RUb02X71YFOTxm1%2FWYygCTUGSOtMU%3D; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1502168619,1502169023,1502171025,1502179520; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1502180017',
           'Host': 'www.oschina.net',
           'Origin': 'http://www.oschina.net',
           'Referer': 'http://www.oschina.net/',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest'
           }

web_data = requests.post('http://www.oschina.net/widgets/index_tweet_list', headers=headers)
web_data.encoding = 'utf-8'

doc = pq(web_data.text)
t = doc('.tweet-content').text()

d = path.dirname(__file__)  # # # Read the whole text.
# # text = open(path.join(d, 'yes_minister.txt'), encoding='utf-8').read()

My_text = jieba.cut(t, cut_all=True)

wl_space_split = " ".join(My_text)

alice_coloring = np.array(Image.open(path.join(d, "xiaohuangren.jpg")))
stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="black", max_words=2000, mask=alice_coloring,
               stopwords=stopwords, max_font_size=40, font_step=1, random_state=42,
               font_path='C:\Windows\Fonts\msyhbd.ttc')

wc.generate(My_text)

# create coloring from image
image_colors = ImageColorGenerator(alice_coloring)

plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.show()
wc.to_file("cloud.png")
