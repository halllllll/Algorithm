# 自分をiとしたとき自分よりあとのjと比べj-iが最大になる箇所の数を数える、という感じ
# （Tは不要？） b
# A[i]はユニークなので
# 左から最小、右から最大を保存?（なんでこれが浮かんだ？）
#       7 10 4 5 9 3 6 8 2 1
# 最小:  7 7 4 4 4 3 3 3 2 1
# 最大: 10 10 9 9 9 8 8 8 2 1
# dif maxの数になる
# だるそうなので集合でやる（ユニークなので）
n, t = map(int, input().split())
arr = list(map(int, input().split()))
min_from_left, max_from_right = [arr[0]], [arr[-1]]
for i in range(1, n):
    min_from_left.append(min(min_from_left[i - 1], arr[i]))
    max_from_right.append(max(max_from_right[i - 1], arr[n - 1 - i]))

max_from_right = max_from_right[::-1]
max_dif = 0
difs = set()
for i in range(n - 1):
    if max_dif < max_from_right[i + 1] - min_from_left[i]:
        max_dif = max_from_right[i + 1] - min_from_left[i]
        difs = set()
        difs.add((max_from_right[i + 1], min_from_left[i]))
    elif max_dif == max_from_right[i + 1] - min_from_left[i]:
        difs.add((max_from_right[i + 1], min_from_left[i]))
print(len(difs))