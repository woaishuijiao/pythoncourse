#TextProBarV3.py
import time
scale = 40
str = '>'
print("执行开始".center(scale // 2, '-'))
start = time.perf_counter()
for i in range(scale + 1):
    a = '=' * i
    b = '.' * (scale - i)
    c = (i / scale)
    dur = time.perf_counter() - start
    if (1 == c):
        str = '='
    print("\r{:<6.1%}[{}{}{}] {:.2f}s".format(c, a, str, b, dur), end='')
    time.sleep(0.1)
print("\n" + "执行结束".center(scale // 2, '-'))