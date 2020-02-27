# 最短でゴールして残った黒をぜんぶ白に変えれば最大のポイントをもらえそう
# ってなふうに雑に考えてたけど、探索・最短経路復元・解答それぞれで1度ずつBFSをしなきゃならんのか？？？？

h, w = map(int, input().split())
table = [[] for _ in range(h)]
for y in range(h):
    table[y] = list(input())
# ステップ更新用
my_table = [[-1 for _ in range(w)] for _ in range(h)]
my_table[0][0] = 0
yo = [(0, 0)]
steps = [0, -1, 0, 1, 0]
while len(yo) > 0:
    p = yo[0]
    yo = yo[1:]
    for i in range(4):
        next_x, next_y = steps[i + 1] + p[1], steps[i] + p[0]
        if next_x < 0 or w <= next_x or next_y < 0 or h <= next_y:
            continue
        if table[next_y][next_x] == "#":
            continue
        if my_table[next_y][next_x] >= 0:
            continue
        my_table[next_y][next_x] = my_table[p[0]][p[1]] + 1
        yo.append((next_y, next_x))
if my_table[h - 1][w - 1] == -1:
  print(-1)
  exit()
  
# 経路を逆からたどって最短経路復元
restore_table = [["o" for _ in range(w)] for _ in range(h)]
restore_table[h - 1][w - 1] = "x"
now = my_table[h - 1][w - 1]
cur = (h - 1, w - 1)
while now != 0:
    for i in range(4):
        next_y, next_x = steps[i] + cur[0], steps[i + 1] + cur[1]
        if next_x < 0 or w <= next_x or next_y < 0 or h < next_y:
            continue
        if my_table[next_y][next_x] == now - 1:
            restore_table[next_y][next_x] = "x"
            cur = (next_y, next_x)
            now -= 1
            break

# やっと答え
ans = 0
for y in range(h):
    for x in range(w):
        if restore_table[y][x] == "o" and table[y][x] == ".":
            ans += 1
print(ans)
