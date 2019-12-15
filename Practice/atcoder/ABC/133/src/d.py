# (d1+d2)/2 == n1, (d2+d3)/2 == n2... が矛盾なくなるようにする
import bisect
n = int(input())
a = list(map(int, input().split()))

cur = 0
x = 0
while True:
    pre = cur
    ans = [0 for _ in range(n)]
    ans[0] = cur
    for i in range(n-1):
        cur = a[i] * 2 - cur
        ans[i+1] = cur
        if cur < 0:
            break
    if a[-1] * 2 == cur + pre:
        print(" ".join(list(map(str, ans))))
        break
    x += 1
    cur = x * 2
