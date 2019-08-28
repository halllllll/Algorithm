# DP
N, M = map(int, input().split())

D, V = [], []
for _ in range(N):
    x = list(map(int, input().split()))
    D.append(x[0])
    V.append(x[1])

print(D, V)

# なぜかうまくいかない
# def f(i, c, d, k):
#     if k == M:
#         return c
#     if i == N:
#         return -1
#     if d + D[i] > N:
#         return f(i + 1, c, d, k)
#     return max(f(i + 1, c + V[i], d + D[i], k + 1), f(i + 1, c, d, k))


# print(f(0, 0, 0, 0))

