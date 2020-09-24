n = int(input())
a = list(map(int, input().split()))
ans = 0
cur = a[0]
for i in range(1, n):
    if cur <= a[i]:
        cur = a[i]
    else:
        ans += cur - a[i]
        a[i] = cur
        cur = a[i]
print(ans)