# 愚直にやってもどうせ間に合う


n = int(input())


def keta(x):
    k = 0
    while x > 0:
        x //= 10
        k += 1
    return k


ans = 0
for i in range(n, 0, -1):
    if keta(i) % 2 == 1:
        ans += 1


print(ans)
