# 横を決めれば縦がきまるし余るタイルも決まる
n = int(input())
ans = 10 ** 10
for i in range(1, n + 1):
    j = n // i
    amari = n - (i * j)
    ans = min(ans, abs(i - j) + amari)
print(ans)
