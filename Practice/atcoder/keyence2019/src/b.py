# keyenceが先頭にある場合と最後にある場合、それ以外は真ん中にある場合
s = input()
keyence = "keyence"
for i in range(len(keyence)):
    if s[: i + 1] == keyence[: i + 1] and s[-i + 1 :] == keyence[-i + 1]:
        print("YES")
        exit()
print("NO")
