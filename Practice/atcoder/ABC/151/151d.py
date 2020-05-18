from collections import deque
from copy import deepcopy
h, w = map(int, input().split())
table = [[] for _ in range(h)]
for i in range(h):
    table[i] = list(input())

steps = [0, 1, 0, -1, 0]
ans = 0
for y in range(h):
    for x in range(w):
        if table[y][x] == "#":
            continue
        t = deepcopy(table)
        t[y][x] = 0
        queue = deque()
        queue.append((y, x))
        while len(queue) > 0:
            cur = queue.popleft()
            for i in range(4):
                ny, nx = cur[0] + steps[i], cur[1] + steps[i + 1]
                if 0 <= ny and ny < h and 0 <= nx and nx < w and t[ny][
                        nx] == ".":
                    t[ny][nx] = t[cur[0]][cur[1]] + 1
                    queue.append((ny, nx))
        tmp = 0
        for i in range(h):
            for j in range(w):
                if str(t[i][j]).isnumeric():
                    tmp = max(tmp, t[i][j])
        ans = max(ans, tmp)
print(ans)