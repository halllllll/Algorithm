# 和の期待値は期待値の和
# それぞれ期待値を出したあとは大きさKの区間和の最大値
# n(n+1)/2
n, k = map(int, input().split())
p = []
for x in list(map(int, input().split())):
    p.append((x * (x + 1) // 2) / x)

ans = 0
tmp = 0
for i in range(n):
    tmp += p[i]
    if i >= k:
        tmp -= p[i - k]
    ans = max(ans, tmp)

print(ans)