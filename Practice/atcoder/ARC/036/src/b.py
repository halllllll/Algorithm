# しゃくとりの臭いがするが
# 単調増加からの単調減少が長いところを探す
# 累積でもいけるか？
# けっこう雑にやったんだけど通った よっしゃ
n = int(input())
hs = [int(input()) for _ in range(n)]
from_left = [0] * (n + 1)
from_right = [0] * (n + 1)
for i in range(1, n):
    if hs[i - 1] < hs[i]:
        from_left[i] = from_left[i - 1] + 1
    else:
        from_left[i] = 0
for i in range(n - 2, -1, -1):
    if hs[i] > hs[i + 1]:
        from_right[i] = from_right[i + 1] + 1
    else:
        from_right[i] = 0

ans = 0
for i in range(n + 1):
    ans = max(ans, from_left[i] + from_right[i] + 1)
print(ans)