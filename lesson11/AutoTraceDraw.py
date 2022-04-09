#AutoTraceDraw.py
import turtle as t
t.title("自动轨迹绘制")
t.setup(800, 800)
t.pencolor('red')
t.pensize(5)
datas = []
f = open("data.txt")
for line in f:
    line = line.replace("\n", "")
    datas.append(list(map(eval, line.split(','))))
f.close()
for i in range(len(datas)):
    ls = datas[i]
    t.pencolor(ls[3], ls[4], ls[5])
    t.fd(ls[0])
    t.left(ls[2]) if ls[1] == 0 else t.right(ls[2])
t.done()