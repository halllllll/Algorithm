n, d = map(int, input().split())
points = []
for _ in range(n):
    points.append(list(map(int, input().split())))

ans = 0
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        dif = 0
        for k in range(d):
            dif += abs(points[i][k] - points[j][k]) ** 2
        if dif ** 0.5 == int(dif ** 0.5):
            ans += 1
print(ans)
