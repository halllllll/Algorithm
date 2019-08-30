# 一回で回していくバージョン
r, c = map(int, input().split())
sheet = [[0 for _ in range(c)] for _ in range(r)]
last_culmn = [0 for _ in range(c)]
s = 0
for y in range(r):
    row = list(map(int, input().split()))
    row_s = 0
    for x in range(c):
        sheet[y][x] = row[x]
        row_s += row[x]
        last_culmn[x] += row[x]
        s += sheet[y][x]
    sheet[y].append(row_s)
last_culmn.append(s)
sheet.append(last_culmn)

[print(" ".join(list(map(str, line)))) for line in sheet]
