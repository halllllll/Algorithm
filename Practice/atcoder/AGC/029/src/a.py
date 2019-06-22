# 最終形態はWwWW...BBB...
# Wが左に詰めて移動する距離の総数
s = input()
ans = 0
wc = 0
for si, sv in enumerate(s):
    if sv == "W":
        ans += si - wc
        wc += 1
print(ans)
