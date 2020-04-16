n = int(input())
arr = list(map(int, input().split()))

# nC2:
# 1(i=2)
# 3(i=3)
# 6(i=4)
# 10(i=5)
# 15(i=6)
# 21(i=7)
# 28(i=8)
# 36(i=9)

def ncr(n, r):
    res = 1
    for i in range(1, r + 1):
        res = res * (n - i + 1) // i
    return res

nc2s = {}
for i in range()

d = {}
for a in arr:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

memo = {}
for k, v in d.items():
    if k not in memo:
        x = ncr(v, 2)
        memo[k] = x
for a in arr:
    print(memo[a])
