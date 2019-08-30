"""
input
4
13 25
7 3
11 38
4 50
output
(x, y)を座標圧縮する
"""
n = int(input())
data = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    data.append((x, y))
print(data)
# (インデックス, 値)で値でソート
datax = sorted(enumerate(list(zip(*data))[0]), key=lambda x:x[1])
datay = sorted(enumerate(list(zip(*data))[1]), key=lambda x:x[1])
res = []
for i in range(n):
    res.append((datax[i][0], datay[i][0]))
print(res)
