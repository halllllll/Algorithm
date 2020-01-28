# 尺取かと思ったけど実装できんな
# あれ？過半数だから成立する場合は3文字だけを抜き取ったどこかで必ず成立するのでは
s = input()
if len(s) == 2:
    if s[0] == s[1]:
        print(1, 2)
    else:
        print(-1, -1)
    exit()
for i in range(len(s) - 3):
    target = s[i : i + 3]
    if target[0] == target[1] or target[1] == target[2] or target[2] == target[0]:
        print(i + 1, i + 3)
        exit()
print(-1, -1)
