# いつもの探索でいいです 終了

h, w = map(int, input().split())
table = []
for _ in range(h):
  table.append(list(input()))

for i in range(h):
  for j in range(w):
    if table[i][j] != "#":
      sub_h = [0] if h==1 else [-1, 0, 1] if 0<i<h-1 else [0, 1] if i==0 else [-1, 0]
      sub_w = [0] if w==1 else [-1, 0, 1] if 0<j<w-1 else [0, 1] if j==0 else [-1, 0]
      count = 0
      for sh in sub_h:
        for sw in sub_w:
          if sh == sw == 0:
            continue
          if table[i+sh][j+sw] == "#":
            count += 1
      table[i][j] = str(count)

for i in range(h):
  print("".join(table[i]))