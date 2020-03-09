# 全探索 行列だとNがでかすぎて死にそうなのでリストでやる
# 偶奇だけわかればいいので%2する（必要ないけど）
# w=奇数のとき両辺のとりうるのは(1,0)か(0,1)で、ここからキメたほうがよさそう?
# 距離をどういうデータ構造でもてばいいのかわからんぞ....
# あ？偶数と奇数をわけて最初に偶数をキメて次に奇数をキメるのでいいのか？
n = int(input())
arr = [-1 for _ in range(n)]
odd, even = [], []
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    if w % 2 == 0:
        even.append([u - 1, v - 1])
    else:
        odd.append([u - 1, v - 1])

for e in even:
    arr[e[0]] = 0
    arr[e[1]] = 0

while len(odd) > 0:
    rest = []
    for o in odd:
        x, y = o
        if arr[x] < 0 and arr[y] < 0:
            rest.append(o)
        elif arr[x] == 0:
            arr[y] = 1
        elif arr[x] == 1:
            arr[y] = 0
        elif arr[y] == 0:
            arr[x] = 1
        elif arr[y] == 1:
            arr[x] = 0
        else:
            print("fuck")
            print(4 / 0)
    odd = rest
for a in arr:
    print(a)
