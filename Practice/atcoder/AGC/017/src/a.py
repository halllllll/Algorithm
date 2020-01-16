# P=0 -> 奇数を偶数個といくつかの偶数個
# P=1 -> 奇数を奇数個といくつかの奇数個
# 1000回くらいWAしたのでどんどんアドホックになっていった

n, p = map(int, input().split())
odds = n - len(list(filter(lambda x: int(x) % 2 == 0, input().split())))
evens = n - odds


def ncr(n, r):
    res = 1
    for i in range(1, r + 1):
        res = res * (n - i + 1) // i
    return res


ans = 0
if p == 0:
    for i in range(0, odds + 1, 2):
        ans += ncr(odds, i)
    if evens > 0:
        ans *= max(1, 2 ** evens)
else:
    if odds > 0:
        for i in range(1, odds + 1, 2):
            ans += ncr(odds, i)
        ans *= max(1, 2 ** evens)
print(ans)
