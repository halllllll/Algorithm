# にほんごがやさしい
# S->1->2->..N-1->Nという感じで各最短パスをみつけていく

h, w, n = map(int, input().split())
table = []
goals = list(range(n + 1))
for y in range(h):
    line = list(input())
    table.append(line)
    for x in range(w):
        if line[x] == "S":
            goals[0] = (y, x)
        if line[x].isnumeric():
            goals[int(line[x])] = (y, x)
i = 0
ans = 0


def bfs(table, start, goal):
    passed = [[-1 for _ in range(len(table[0]))] for _ in range(len(table))]
    passed[start[0]][start[1]] = 0
    queue = [start[:]]
    steps = [0, 1, 0, -1, 0]
    while True:
        cur = queue[0]
        queue = queue[1:]
        if cur == goal:
            break
        for i in range(4):
            next_y, next_x = steps[i] + cur[0], steps[i + 1] + cur[1]
            if next_x < 0 or w <= next_x or next_y < 0 or h <= next_y:
                continue
            if table[next_y][next_x] == "X":
                continue
            if passed[next_y][next_x] >= 0:
                continue
            queue.append((next_y, next_x))
            passed[next_y][next_x] = passed[cur[0]][cur[1]] + 1
    return passed[goal[0]][goal[1]]


while i < n:
    s, g = goals[i], goals[i + 1]
    ans += bfs(table, s, g)
    i += 1
print(ans)

