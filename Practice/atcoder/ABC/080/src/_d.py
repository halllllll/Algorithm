# N個のimosなので二次元でやる 0.5がうざいので*2する( (2*10^5) * C )

# なぜか2WAが取れない

N, C = map(int, input().split())
x = 2 * (10 ** 5)

imos = [[0 for _ in range(x)] for _ in range(C)]
for _ in range(N):
    s, t, c = map(int, input().split())
    s, t, c = s * 2 - 1, t * 2 - 1, c - 1
    imos[c][s - 1] += 1
    imos[c][t] -= 1


for i in range(C):
    for j in range(1, x):
        imos[i][j] += imos[i][j - 1]

ans = 0
for j in range(x):
    tmp = 0
    for i in range(C):
        tmp += imos[i][j]
    ans = max(ans, tmp)

print(ans)

# 1 3
# 3 4 2
