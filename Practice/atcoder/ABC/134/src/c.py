# 最大値はひとつだけ、自分自身が最大値の場合を除く

n = int(input())
max_a, max_ai = 0, 0
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)
    if a > max_a:
        max_a = a
        max_ai = i + 1
arr = sorted(arr)

for i in range(n):
    if max_ai == i + 1:
        print(arr[-2])
    else:
        print(max_a)

