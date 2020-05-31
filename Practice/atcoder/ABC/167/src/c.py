# Nについての全探索でいけそう
n, m, x = map(int, input().split())
cost, A = [0] * n, [[]] * n
for i in range(n):
    line = list(map(int, input().split()))
    cost[i] = line[0]
    A[i] = line[1:]

ans = 10**10

for bit in range(1 << n):
    tmp_cost = 0
    tmp_a = [0] * m
    for i in range(n):
        if bit >> i & 1 == 1:
            tmp_cost += cost[i]
            for j in range(m):
                tmp_a[j] += A[i][j]
        # すべてXを越えてるかチェック filterがどこにあるかわからんw
    if len(list(filter(lambda t: t >= x, tmp_a))) == m:
        ans = min(ans, tmp_cost)
print(ans if ans != 10**10 else -1)