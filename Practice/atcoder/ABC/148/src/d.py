# 左から1, 2, 3...と出現すればいい
n = int(input())
lis = list(map(int, input().split()))
tmp = 0
c = 0
for a in lis:
    if tmp + 1 == a:
        c += 1
        tmp += 1
if c == 0:
    print(-1)
else:
    print(n - c)

