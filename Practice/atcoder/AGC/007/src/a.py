# 右と下の両方に#があったら終了だしどちらにもなくても終了
# なんやこのクソみたいな実装は

h, w = map(int, input().split())
table = []
sharp = 0
for _ in range(h):
    get = input()
    table.append(get)
    sharp += get.count("#")

flag = False
pos = [0, 0]
path = 0
while True:
    if pos == [h - 1, w - 1]:
        path += 1
        flag = True
        break
    if h <= pos[0] or w <= pos[1]:
        break
    if (
        pos[0] < h - 1
        and pos[1] < w - 1
        and table[pos[0] + 1][pos[1]] == "#"
        and table[pos[0]][pos[1] + 1] == "#"
    ):
        break
    if pos[0] < h - 1 and pos[1] < w - 1 and table[pos[0] + 1][pos[1]] == "#":
        pos[0] += 1
        path += 1
        continue
    elif pos[0] < h - 1 and pos[1] < w - 1 and table[pos[0]][pos[1] + 1] == "#":
        pos[1] += 1
        path += 1
        continue
    if pos[0] == h - 1 and pos[1] < w - 1 and table[pos[0]][pos[1] + 1] == "#":
        pos[1] += 1
        path += 1
        continue
    elif pos[0] < h - 1 and pos[1] == w - 1 and table[pos[0] + 1][pos[1]] == "#":
        pos[0] += 1
        path += 1
        continue
    else:
        break

print("Possible" if flag and path == sharp else "Impossible")
