# 1. 両端にaもbも含まれないもしくは「先頭がaで末尾がb」は分けて考える 最後にテキトーに加えてやる
# 2. 「先頭がb」「末尾がa」「先頭がbで末尾がa」
# cca
# caa
# bac
# bbc
# bccca < -これは連結したほうがよさそう連結したあとに左にooa右にbooを加える
# あまったooaとbooで適当にくっつける
n = int(input())
ans = 0
both = 0
a, b = 0, 0
for _ in range(n):
    s = input()
    if s[0] != "B" and s[-1] != "A":
        ans += s.count("AB")
    else:
        if s[0] == "B" and s[-1] == "A":
            both += 1
            ans += s.count("AB")
        elif s[0] == "B":
            b += 1
            ans += s.count("AB")
        elif s[-1] == "A":
            a += 1
            ans += s.count("AB")
# 両脇にあるやつを連結
if both > 0:
    ans += both - 1
    # 連結したやつの先頭に加えられたら加える
    if a > 0:
        ans += 1
        a -= 1
    # 同じく末尾
    if b > 0:
        ans += 1
        b -= 1
# 余ったやつで作成
ans += min(a, b)
print(ans)
