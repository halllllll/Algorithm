from copy import deepcopy
from collections import deque

# 最短にする
# 0回以上でたどり着けるのでスタート=ゴールのことがある ふざけんな
h, w = map(int, input().split())
table = [[] for _ in range(h)]
for i in range(h):
    table[i] = list(input())


def bfs(y, x, t):
    steps = [0, 1, 0, -1, 0]
    queue = deque([[y, x]])
    ret = 0
    while len(queue) > 0:
        cur_y, cur_x = queue.popleft()
        for i in range(4):
            next_y, next_x = cur_y + steps[i], cur_x + steps[i + 1]
            if 0 <= next_y < h and 0 <= next_x < w:
                if t[next_y][next_x] == ".":
                    t[next_y][next_x] = t[cur_y][cur_x] + 1
                    ret = max(ret, t[next_y][next_x])
                    queue.append([next_y, next_x])

    return ret


ans = 0
for sy in range(h):
    for sx in range(w):
        # table[sy][sx]をスタート地点とする
        if table[sy][sx] != ".":
            continue
        mytable = deepcopy(table)
        mytable[sy][sx] = 0
        ret = bfs(sy, sx, mytable)
        ans = max(ans, ret)

print(ans)
