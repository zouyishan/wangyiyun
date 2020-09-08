import jieba
import numpy as np
from wordcloud import WordCloud
from PIL import Image
from os import path

d = path.dirname(__file__)
alice_coloring = np.array(Image.open(path.join(d, "1.jpg")))

w = WordCloud(width=1920,
              height=1312,
              background_color='black',
              # mask=alice_coloring,
              font_path="simsun.ttf",
              random_state=30)


def stopwordslist():
    stopwords = [line.strip() for line in open('cn_stopwords.txt', encoding='utf-8').readlines()]
    return stopwords


def seg_depart(sentence):
    sentence_depart = jieba.cut(sentence.strip())
    stopwords = stopwordslist()
    outstr = ''
    for word in sentence_depart:
        if word not in stopwords:
            outstr += word
    return outstr

txt = ''
with open('人间失格.txt', encoding="utf-8") as fp:
    lines = fp.readlines()
    for line in lines:
        seg_list = seg_depart(line)
        txt += seg_list

txtlist = jieba.lcut(txt)
string = " ".join(txtlist)
w.generate(string)

w.to_file('人间失格.png')