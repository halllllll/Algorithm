# 同じロジックでなぜかrubyが通らなかったので諦めてpythonでやるだけ
# 超典型mazeの最短
# なぜかpopでとったやつの判定と更新がうまくいかないので仕方なくforでそれやることにした

from collections import deque
h, w = map(int, input().split())


class Pos:
    def __init__(self, y, x, c):
        self.y = y
        self.x = x
        self.c = c


s = list(map(int, input().split()))

start = Pos(s[1]-1, s[0]-1, 0)
goal = list(map(int, input().split()))
table = []
for _ in range(h):
    table.append(list(input().rstrip()))


table[goal[0]-1][goal[1]-1] = "g"

queue = deque([start])
ans = 0
# while len(queue) > 0:
flag = False
while flag == False:
    cur_pos = queue.popleft()
    """
    なぜか判定と更新ががうまくいかないのでfor内でやることにする
    if table[cur_pos.y][cur_pos.x] == "g":
        ans = cur_pos.c
        break
    else:
        table[cur_pos.y][cur_pos.x] = "#"
    """

    steps = [0, 1, 0, -1, 0]
    for i in range(4):
        nex_y, nex_x = cur_pos.y + steps[i], cur_pos.x + steps[i + 1]
        """
        なぜか判定と更新がうまくいかないのでfor内でやることにする
        if table[nex_y][nex_x] != "#":
            print("nex: {}".format(table[nex_y][nex_x]))
            nex_pos = Pos(nex_y, nex_x, cur_pos.c + 1)
            queue.append(nex_pos)
        """
        if table[nex_y][nex_x] == "g":
            # breakするとforしかぬけないのでわざわざフラグを用意してやる
            flag = True
            ans = cur_pos.c + 1
        elif table[nex_y][nex_x] == ".":
            table[nex_y][nex_x] = "#"
            nex_pos = Pos(nex_y, nex_x, cur_pos.c + 1)
            queue.append(nex_pos)

print(ans)
