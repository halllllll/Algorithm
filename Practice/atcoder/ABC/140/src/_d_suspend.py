# なんか似たような問題どっかにあったよね忘れたけど
# 反転させる、がヤバそうだけど、同じ方向を向いてる部分列だけを反転することは単純に別の文字に変えることと同値
# そして、違う方向を向いているのを含む箇所を反転させることは無意味
# 当然ながら連続してるほうが有利
# Kまでのしゃくとりでなんとかならんか となるとLとR両方やらんといかんか
# しゃくとり無限に難しい無理不可能 配列にsplitするわ
n, k = map(int, input().split())
s = input()
lis = []
l, r = 0, 0
tmp = ""
while l < n:
    while r < n and s[l] == s[r]:
        tmp += s[r]
        r += 1
    lis.append(tmp)
    tmp = ""
    l = r  # ワープさせる （ワープ？）

print(lis)
lnh = len(lis)
l_arr, r_arr = [0] * lnh, [0] * lnh
l_sum, r_sum = 0, 0
for i in range(lnh):
    if lis[i][0] == "L":
        l_arr[i] = len(lis[i]) + (l_arr[i - 1] if i > 0 else 0)
        l_sum += len(lis[i])
        r_arr[i] = r_arr[i - 1] if i > 0 else 0
    else:
        r_arr[i] = len(lis[i]) + (r_arr[i - 1] if i > 0 else 0)
        r_sum += len(lis[i])
        l_arr[i] = l_arr[i - 1] if i > 0 else 0
print(l_arr)
print(r_arr)
ans, tmp = 10**10, 0
r = 0
for l in range(lnh):
    while r < lnh and r - l < k * 2:
        tmp += r_arr[r] + l_arr[l]
        r += 1
    if r == lnh:
        break
    tmp -= (l_arr[l] + r_arr[r])
    print(lis[l:r], tmp)
# a-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa