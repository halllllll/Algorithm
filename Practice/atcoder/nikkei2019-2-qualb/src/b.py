# 最初dは与えられる距離だと思ってて「サンプルケース1は3じゃね？」とか思ってて2時間経過した
# 落ち着いて読んだら最小の辺の数だった

from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
if arr[0] != 0:
    print(0)
    exit()
arr = sorted(list(Counter(arr).items()), key=lambda x: x[0])
if arr[0][1] > 1:
    print(0)
    exit()

mod = 998244353
ans = 1
tmp = 1
for i in range(1, len(arr)):
    if arr[i][0] != i:
        print(0)
        exit()
    ans *= pow(tmp, arr[i][1])
    ans %= mod
    tmp = arr[i][1]

print(ans)
