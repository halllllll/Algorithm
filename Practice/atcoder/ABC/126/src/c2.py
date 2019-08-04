# 解き直し
# こっちのが洗練されてるわ

n, k = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    tmp, cnt = i, 0
    while tmp < k:
        tmp *= 2
        cnt += 1
    ans += (1 / n) * (1 / 2) ** cnt
print(ans)
