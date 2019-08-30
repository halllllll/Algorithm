# 解き直し
# 負数が偶数なら全部+にできる 奇数ならすべてを正数にして一番ちいさいやつを引く
n = int(input())
arr = list(map(int, input().split()))
minus_n = 0
positive_arr = list(sorted(list(map(lambda x: abs(x), arr))))
for a in arr:
    if a < 0:
        minus_n += 1

if minus_n % 2 == 0:
    print(sum(positive_arr))
else:
    print(sum(positive_arr) - positive_arr[0] * 2)

