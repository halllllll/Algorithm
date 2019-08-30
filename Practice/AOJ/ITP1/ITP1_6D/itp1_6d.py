n, m = map(int, input().split())
A = [[0 for _ in range(m)] for _ in range(n)]
B = [0 for _ in range(m)]
for y in range(n):
    column = list(map(int, input().split()))
    for x in range(m):
        A[y][x] = column[x]

for x in range(m):
    B[x] = int(input())

for a in A:
    c = 0
    for i in range(m):
        c += a[i]*B[i]
    print(c)
