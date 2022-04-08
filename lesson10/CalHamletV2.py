#CalHamletV2.py
import jieba
txt = open("threekingdoms.txt", "r", encoding="utf-8").read()
excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此", "商议", "如何", "主公", "军士", \
            "左右", "军马", "引兵", "次日", "大喜", "天下", "东吴", "于是", "今日", "不敢", "魏兵", \
            "陛下", "一人", "都督", "人马", "不知", "汉中", "只见", "众将", "后主", "蜀兵", "上马", \
            "大叫", "太守", "此人", "夫人", "先主", "后人", "背后", "城中", "一面", "何不", "天子"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<{2}}{1:>5}".format(word, count, 10-len(word)))