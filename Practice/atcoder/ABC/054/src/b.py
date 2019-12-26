# atcoder problemsからきました
# 全探索
n, m = map(int, input().split())
a, b = [], []
for _ in range(n):
    a.append(list(input()))
for _ in range(m):
    b.append(list(input()))

for i in range(n - m + 1):
    for j in range(n - m + 1):
        target = [["-" for _ in range(m)] for _ in range(m)]
        for y in range(m):
            for x in range(m):
                target[y][x] = a[i + y][j + x]
        if b == target:
            print("Yes")
            exit()
print("No")
