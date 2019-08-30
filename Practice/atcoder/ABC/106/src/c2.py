# 混乱する

s = input()
k = int(input())
for i, v in enumerate(s):
    if int(v) > 1 and i+1 <= k:
        print(v)
        exit()
print(1)
