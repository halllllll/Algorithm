# 最大と最小がわかればpが決まる
n, a, b = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])
minn, maxn = arr[0], arr[-1]
if minn == maxn:
    print(-1)
    exit()
p = b / (maxn - minn)
q = a - p * (sum(arr) / n)
print(p, q)
