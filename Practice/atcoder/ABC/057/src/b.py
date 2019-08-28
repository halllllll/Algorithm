n, m = map(int, input().split())
students = []
for _ in range(n):
    students.append(list(map(int, input().split())))

points = []
for i in range(m):
    c, d = map(int, input().split())
    points.append([c, d, i + 1])


for s in students:
    tmp_d, tmp_i = 10 ** 18, -1
    for p in points:
        dif = abs(s[0] - p[0]) + abs(s[1] - p[1])
        if dif < tmp_d:
            tmp_d = dif
            tmp_i = p[2]
    print(tmp_i)
