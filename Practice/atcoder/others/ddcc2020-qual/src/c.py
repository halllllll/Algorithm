# コンテスト終了後にkyopro_friendsの解説を見て実装した
# 高さ1として各行をやったあとに埋まってない行を上か下からコピーする

h, w, k = map(int, input().split())
table = []
result_table = [["-" for _ in range(w)] for _ in range(h)]
for _ in range(h):
    table.append(list(input()))

# 盤を埋める数
c = 1
for y in range(h):
    line = table[y]
    idx = 0
    if "#" not in line:
        continue
    # 行の残りの部分に#があれば更新する
    while True:
        if "#" in line[idx:]:
            tmp = idx
            idx = line.index("#")
            line[idx] = "済"
            idx += 1
            for j in range(tmp, idx):
                result_table[y][j] = str(c)
            c += 1
        else:
            break
    # 残ってるところを現在のc-1で埋める（上のほうで次のループに備えて+1してるぶんを相殺）
    for j in range(w):
        if result_table[y][j] == "-":
            result_table[y][j] = str(c - 1)

# この時点で残ってるのは`-`で埋まった列
# これは上か下からコピーする 今回は両方からコピーするので番兵がてら最終行と最初の行を増やしとく
# まず下から
result_table.append(result_table[-1])

for i in range(h - 1, -1, -1):
    if result_table[i] == ["-"] * w:
        result_table[i] = result_table[i + 1]

result_table = result_table[:-1]

# 次に上から だるいのでreverse
result_table = result_table[::-1]
result_table.append(result_table[-1])

for i in range(h - 1, -1, -1):
    if result_table[i] == ["-"] * w:
        result_table[i] = result_table[i + 1]

result_table = result_table[:-1]
result_table = result_table[::-1]

for t in result_table:
    print(" ".join(t))

# test
# 3 7 7
# #...#.#
# ..#...#
# .#..#..


# test
# 4 7 6
# .#.#...
# ...#.#.
# .......
# #..#...

# test
# 4 5 4
# .#.#.
# ...#.
# #....
# .....

# test
# 5 5 6
# .....
# #...#
# ...##
# .#.#.
# .....
