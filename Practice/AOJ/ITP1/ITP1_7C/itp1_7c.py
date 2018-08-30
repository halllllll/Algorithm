r, c = map(int, input().split())
sheet = []
c_sum = [0 for _ in range(c)]
for y in range(r):
    sheet.append(list(map(int, input().split())))
    sheet[y].append(sum(sheet[y]))
    # transposeするのはめんどくさいのでループでまわしてみる
    for x in range(c):
        c_sum[x] += sheet[y][x]
    print(" ".join(list(map(str, sheet[y]))))
c_sum.append(sum(c_sum))
print(" ".join(list(map(str, c_sum))))
