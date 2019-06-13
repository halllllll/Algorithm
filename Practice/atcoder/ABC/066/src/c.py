# 適当に1~6くらいまでの数列でやると法則がみえてくるのでそうする
# nが偶数 -> 後ろから偶数番目を降順で、のちに頭から奇数を昇順で
# nが奇数 -> 後ろから奇数番目を降順で、のちに頭から偶数を昇順で

n = int(input())
arr = input().split()
pre, epi = [], []
if n % 2 == 0:
    pre = arr[::-2]
    epi = arr[::2]
else:
    pre = arr[-1::-2]
    epi = arr[1::2]
print(" ".join(pre), end=" ")
print(" ".join(epi))
