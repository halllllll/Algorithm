n = int(input())
a = list(map(int, input().split()))
ans = 0
tmp = 0
r = 0
for l in range(n):
    while r < n and tmp < n:
        tmp += a[r]
        r += 1
    if tmp == n:
        ans += 1
    if r == l:
        r += 1
    else:
        tmp -= a[l]
print(ans)