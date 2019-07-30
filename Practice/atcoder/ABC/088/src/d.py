# #の数を数えておいて、最初の.の数-最短距離
# 最短経路なので幅優先でやる
from collections import deque

h, w = map(int, input().split())
table =[]
default_dot = 0
for _ in range(h):
  line = list(input())
  default_dot+=line.count(".")
  table.append(line)

default_dot-=2  # スタートとゴール
table[0][0] = 0

cur = [0, 0]   # x, y
queue = deque()
queue.append(cur)
steps = [0, 1, 0, -1, 0]

minimum_step = 0

while True:
  if len(queue)==0:
    print(-1)
    exit()
  now = queue.popleft()
  if now[0] == w-1 and now[1] == h-1:
    minimum_step = table[now[1]][now[0]]-1
    break
  for i in range(4):
    next_y, next_x = now[1]+steps[i], now[0]+steps[i+1]
    if 0<=next_y<h and 0<=next_x<w and table[next_y][next_x] == ".":
      table[next_y][next_x] = table[now[1]][now[0]]+1
      queue.append([next_x, next_y])


print(default_dot-minimum_step)