# 1. 左からみていってs[i]=="R" s[i+1]=="L"ではないRの場所を保存
#   その途中でs[i]=="R" s[i+1]=="L" である場所にきたら
#   保存したインデックスとiの差の偶奇でどっちに加えるか判断して+1
# 2. 右からみていってL
# 3. s[i]=="R" s[i+1]=="L"な場所にそれぞれ+1
# 4. 1, 2, 3の同じインデックスを加える

s = input()
n = len(s)

arr = [0 for _ in range(n)]
r_arr = [0 for _ in range(n)]
l_arr = [0 for _ in range(n)]

for i in range(n - 1):
    if s[i] == "R" and s[i + 1] == "L":
        arr[i] += 1
        arr[i + 1] += 1

r_pos = []
for i in range(n - 1):
    if s[i] == "R":
        if s[i + 1] == "L":
            for r in r_pos:
                if (r - i) % 2 == 0:
                    r_arr[i] += 1
                else:
                    r_arr[i + 1] += 1
            r_pos = []
        else:
            r_pos.append(i)
l_pos = []
for i in range(n - 1, 0, -1):
    if s[i] == "L":
        if s[i - 1] == "R":
            for l in l_pos:
                if (l - i) % 2 == 0:
                    l_arr[i] += 1
                else:
                    l_arr[i - 1] += 1
            l_pos = []
        else:
            l_pos.append(i)

ans = [0 for _ in range(n)]
for i in range(n):
    ans[i] = str(arr[i] + r_arr[i] + l_arr[i])

print(" ".join(ans))

