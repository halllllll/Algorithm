n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
# いろいろとめんどくさいので転置します
# B = list(zip(*[list(map(int, input().split())) for _ in range(m)]))
# やっぱやめます
B = [list(map(int, input().split())) for _ in range(m)]
for i in range(n):
    line = []
    for j in range(l):
        ele = 0
        for k in range(m):
            ele += A[i][k]*B[k][j]
        line.append(ele)
    print(" ".join(list(map(str, line))))
