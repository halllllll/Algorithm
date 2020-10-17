h, w = map(int, input().split())
v = "#" * (w + 2)
t = []
t.append(list(v))
for _ in range(h):
    s = "#" + input() + "#"
    t.append(list(s))
t.append(list(v))
ans = 0
steps = [0, 1, 0, -1, 0]
for y in range(h + 2):
    for x in range(w + 2):
        if t[y][x] == "#":
            continue
        tmp = 0
        for i in range(4):
            ny, nx = y + steps[i], x + steps[i + 1]
            if t[ny][nx] == ".":
                tmp += 1
        ans += tmp / 2
print(int(ans))