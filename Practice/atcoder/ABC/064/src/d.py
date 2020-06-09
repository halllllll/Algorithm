# は？
# 挿入とか言っときながら両端に加えることしかできなさそう(理屈は不明)
# 479836982452回やってもわからん ほぼ勘とサンプルの試行錯誤でガチャっただけ
n = int(input())
s = list(input())
surplus_left, surplus_right = 0, 0
right_count, left_count = 0, 0
for i in range(n - 1, -1, -1):
    if s[i] == "(":
        if left_count > 0:
            left_count -= 1
        else:
            surplus_left += 1
    else:
        left_count += 1
for i in range(n):
    if s[i] == ")":
        if right_count > 0:
            right_count -= 1
        else:
            surplus_right += 1
    else:
        right_count += 1

print("(" * surplus_right + "".join(s) + ")" * surplus_left)
