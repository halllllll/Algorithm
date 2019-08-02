# 単純に真ん中でよくない？ -> ダメです 愚直にやりましょう
n = int(input())
s = input()

tmp = 0
for i in range(n):
    x, y = list(s[:i]), list(s[i:])
    tmp = max(tmp, len(set(x) & set(y)))
print(tmp)
