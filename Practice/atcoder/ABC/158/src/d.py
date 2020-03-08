# 先頭と末尾を保ちつつ
from collections import deque

s = input()
q = int(input())
x, y = deque(), deque()
r = 0
for _ in range(q):
    query = input().split()
    if query[0] == "1":
        r += 1
        x, y = y, x
    elif query[0] == "2":
        f, c = query[1], query[2]
        if f == "1":
            if r % 2 == 0:
                x.appendleft(c)
            else:
                x.append(c)
        elif f == "2":
            if r % 2 == 1:
                y.appendleft(c)
            else:
                y.append(c)

if r % 2 == 1:
    s = s[::-1]
    x = reversed(x)
    y = reversed(y)
print("".join(x) + s + "".join(y))
