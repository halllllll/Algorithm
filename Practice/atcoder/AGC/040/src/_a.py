# しゃくとり しゃくとってやらぁ >...><のとき0にリセットしたい、このときの左端lは帳尻合わせする
# 実装がわからん なんだこれ 無理

a = input()
l, r = 0, 0
ans = 0
pre_top = 0
climb, down = 0, 0
while l < len(a):
    while r < len(a) and a[l] == a[r]:
        r += 1
    if a[l] == "<":
        ans += (r - l) * (1 + (r - l)) // 2  # 等差数列の和 初項1公差1末項r-l長さr-l
    else:
        print(l, r)
        ans += 0
    if pre_top < r - l:
        print("今回のを採用 -> {}".format(r - l))
    elif pre_top > r - l:
        print("前回のを利用 -> {}".format(pre_top))
        pre_top = -1
    else:
        print("前回と今回同じ高さだったわ")
    pre_top = max(pre_top, r - l)
    print([i for i in range(1, r - l + 1)])
    l = r
print(ans)