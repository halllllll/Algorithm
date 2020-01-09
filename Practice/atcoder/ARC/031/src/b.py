# それぞれのマスを埋めたときに可能かどうか全探索
# なんか入力おかしない？？？最初にタブがはいるんだが？？？？

from copy import deepcopy

table = []
oh = 0
for i in range(10):
    gets = list(input().split())
    for c in gets:
        table.append(list(c))
        oh += list(c).count("o")


def check(t, sy, sx):
    pos = [(sy, sx)]
    t[sy][sx] = "-"
    o_count = 1
    while len(pos) > 0:
        cur_pos = pos.pop()
        steps = [0, 1, 0, -1, 0]
        for i in range(4):
            if 0 <= cur_pos[0] + steps[i] < 10 and 0 <= cur_pos[1] + steps[i + 1] < 10:
                next_pos = (cur_pos[0] + steps[i], cur_pos[1] + steps[i + 1])
                if t[next_pos[0]][next_pos[1]] == "o":
                    pos.append(next_pos)
                    # 探索済みの印
                    t[next_pos[0]][next_pos[1]] = "-"
                    o_count += 1
    # print("[{}, {}]を埋めた場合の o_count = {}".format(y, x, o_count))
    # print("探索後のtable")
    if o_count == oh + 1:
        return True
    else:
        return False


for y in range(10):
    for x in range(10):
        if table[y][x] == "o":
            continue
        test_table = deepcopy(table)

        test_table[y][x] = "o"
        if check(test_table, y, x):
            print("YES")
            exit()
print("NO")
