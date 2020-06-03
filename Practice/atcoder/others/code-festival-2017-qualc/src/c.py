# x無視したやつが回文なってればいいんじゃね？
# 真ん中にしたい(x以外の)文字が決まれば、もとのsにインデックスを適応して、左右のxの数の差をとればいい
# と思ったけど差をとっただけだと駄目だな xaaxxxbxxcxxxxbxaxxaxx はこの考えだと3だけど実際は7だし
# もうしかたねぇから無理やりsplitした（アホか？）
# これでいけると思いきや駄目 abxxxbaとかでエラーになる
# 趣向を変えて、両脇から比較していくことにしてみる

s = input()
# めんどくさいけどここで確実になるときのやつと回文にならんときのやつを判定すっか
if len(s) == 1:
    print(0)
    exit()
t = ""
for sv in s:
    if sv != "x":
        t += sv
if t != t[::-1]:
    print(-1)
    exit()

l, r = 0, len(s) - 1
ls, rs = "", ""
ans = 0
x = False
while l < r:
    if s[l] == s[r]:
        ls += s[l]
        rs += s[r]
        l += 1
        r -= 1
    else:
        if s[l] == "x":
            while l < r and s[l] != s[r]:
                l += 1
                ans += 1
        else:
            while l < r and s[r] != s[l]:
                r -= 1
                ans += 1
print(ans)
