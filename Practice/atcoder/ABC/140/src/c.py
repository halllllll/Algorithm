# 後ろからみていって最小値or0で更新
n = int(input())
b = list(map(int, input().split()))
a = [10 ** 5 for _ in range(n)]  # どうせ後で更新されるので
a[-1] = b[-1]

for i in range(n - 2, -1, -1):
    a[i] = min(a[i], b[i])
    a[i + 1] = min(a[i + 1], a[i])
print(sum(a))
