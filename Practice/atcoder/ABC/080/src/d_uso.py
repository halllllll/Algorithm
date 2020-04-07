# N個のimosなので二次元でやる 0.5がうざいので*2する( (2*10^5) * C )

# これ嘘解法ぽい気がする

N, C = map(int, input().split())
x = 2 * (10**5)
# x = 30  # test
imos = [[0 for _ in range(x)] for _ in range(C)]
for _ in range(N):
    s, t, c = map(int, input().split())
    s, t, c = s * 2 - 1, t * 2 - 1, c - 1
    imos[c][s - 1] += 1
    imos[c][t] -= 1
    # imos[c][s - 1] = min(1, imos[c][s - 1])  # test

for i in range(C):
    for j in range(1, x):
        imos[i][j] += imos[i][j - 1]
        # imos[i][j] = min(1, imos[i][j])  # test

ans = 0
for j in range(x):
    tmp = 0
    for i in range(C):
        tmp += min(1, imos[i][j])  # 明らかにUSO
    ans = max(ans, tmp)
# print("-----------")
# for x in imos:
#     print(x)
print(ans)

# 1 3
# 3 4 2
