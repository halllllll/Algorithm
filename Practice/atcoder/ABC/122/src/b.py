s = input()


atgc = ["A", "T", "G", "C"]
cnt = 0
for i in range(len(s)):
    tmp = 0
    for j in range(i, len(s)):
        if s[j] in atgc:
            tmp += 1
        else:
            break
    cnt = max(cnt, tmp)

print(cnt)
