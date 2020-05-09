# DPっぽい
import sys
sys.setrecursionlimit(10**8)
N = int(input())
p = []
for _ in range(N):
    w, h = map(int, input().split())
    p.append([w, h])

# 横基準と横基準を探索
P = list(sorted(p, key=lambda x: x[0]))
P2 = list(sorted(p, key=lambda x: x[1]))


def f(i, c_w, c_h, c, p):
    if i == N:
        return c
    if p[i][0] > c_w and p[i][1] > c_h:
        return max(f(i + 1, p[i][0], p[i][1], c + 1, p),
                   f(i + 1, c_w, c_h, c, p))
    else:
        return f(i + 1, c_w, c_h, c, p)


ans = f(1, P[0][0], P[0][1], 1, P)
ans2 = f(1, P2[0][0], P2[0][1], 1, P2)
print(max(ans, ans2))
