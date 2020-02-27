# Bを基準に、それ以前に出てきたAor?とそれ以後に出てくるCor?をかけあわせる感じでやる
# imosっぽくやろうとしたけど問題文を読み違えていて解けず

s = input()
lnh = len(s)
ans = 0
a_foward = [0 for _ in range(lnh)]
if s[0] == "A" or s[0] == "?":
    a_foward[0] = 1
c_back = [0 for _ in range(lnh)]
if s[lnh - 1] == "C" or s[lnh - 1] == "?":
    c_back[lnh - 1] = 1

for i in range(1, lnh):
    if s[i] == "A" or s[i] == "?":
        a_foward[i] = a_foward[i - 1] + 1
    else:
        a_foward[i] = a_foward[i - 1]
    if s[lnh - i - 1] == "C" or s[lnh - i - 1] == "?":
        c_back[lnh - i - 1] = c_back[lnh - i] + 1
    else:
        c_back[lnh - i - 1] = c_back[lnh - i]

print(a_foward)
print(c_back)

for i in range(1, lnh - 1):
    if s[i] == "B" or s[i] == "?":
        print("a :{}通り, c :{}通り".format(a_foward[i - 1], c_back[i + 1]))
        ans += (a_foward[i - 1]) + (c_back[i + 1])
        ans %= 10 ** 9 + 7
        print("現在 {}".format(ans))
print(ans)
