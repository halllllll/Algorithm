# 書き換える枚数は確定できる
# cの大きい順にしたものでaの小さい順にしたものを置き換えるイメージ

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

bcs = []
for _ in range(m):
    bc = list(map(int, input().split()))
    bcs.append(bc)

bcs = sorted(bcs, key=lambda x: x[1], reverse=True)
ans = 0

i = 0
for b in bcs:
    while i < n and arr[i] < b[1] and b[0] > 0:
        ans += b[1]
        b[0] -= 1
        i += 1
print(ans + sum(arr[i:]))
