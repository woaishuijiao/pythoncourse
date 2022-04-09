#GovRptWordCloudv1.py
from ntpath import join
from turtle import width
import jieba
import wordcloud
# f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
f = open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
for word in ls:
    if len(word) == 1:
        ls.remove(word)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path = "msyh.ttc", \
    width = 1000, height = 700, background_color = "white", \
    max_words = 15)
w.generate(txt)
w.to_file("grwordcloud.png")