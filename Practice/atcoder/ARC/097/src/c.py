# 最小かつ最長はzzzzzなので各文字+4まで調べてみるか（27^5-1で全探索もできると思うがやり方がわからん
s = input()
k = int(input())
d = set()
for i in range(len(s)):
    for j in range(1, 6):
        if i + j <= len(s):
            d.add(s[i : i + j])
print(sorted(list(d))[k - 1])
