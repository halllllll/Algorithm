# 頭からみていって違う色がきたら先頭にその色を置くことでそこまでの色はすべて同じにできる
s = input()
count = 0
for si in range(1, len(s)):
    if s[si - 1] != s[si]:
        count += 1
print(count)
