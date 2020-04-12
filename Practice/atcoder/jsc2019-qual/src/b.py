# つよいさんすう （ACしたけど想定解とは違うらしい）
# 最初のAを単独で考えたらいける 等差数列の和の公式はググった
# ex) k = 3, a = [1, 3, 2]
# 1 3 2 1 3 2 1 3 2
# 最初の1 3 2
# 3...[2,1,2,1,2]で5
# 2...[1.1]で2
# 二番目の1 3 2
# 3...[2,1,2]
# 2...[1]
# 三番目の1 3 2
# 3...[2]で1

# 3だけでみると初項1 末項5 公差2で n(2*a1 +(n-1)*2)/2 = 3*(2*1 + (3-1)*2)/2 = 3*6/2 = 9
# n*(a1+an)/2 = 3*(1+5)/2 = 9
# これを一般化すればいけそう

# ex) k = 3, a = [3, 5, 2, 4, 1]とすると
# 3 5 2 4 1 3 5 2 4 1 3 5 2 4 1
# 3の初項は2で公差2 -> 3*(2*2+(3-1)*2)/2 = 12 (6+4+2)
# 5の初項は3で公差4 -> 3*(2*3 + (3-1)*4)/2 = 21 (11+7+3)
# 2の初項は1で公差2 -> 3*(2*1 + (3-1)*2)/2 = 9
# 4の初項は1で公差2 -> 3*(2*1 + (3-1)*3)/2 = 12
# 1の初項は0で公差0 -> 3*(2*0 + (3-1)*0)/2 = 0
# ...みたいな感じ

n, k = map(int, input().split())
a = list(map(int, input().split()))
MOD = 10**9 + 7
first_subarr = [0] * n
rest_arr = [0] * n
for i in range(n):
    for j in range(i, n):
        if a[i] > a[j]:
            first_subarr[i] += 1

for i in range(n - 1, -1, -1):
    for j in range(i, -1, -1):
        if a[j] < a[i]:
            rest_arr[i] += 1

diffs = [0] * n
for i in range(n):
    diffs[i] = first_subarr[i] + rest_arr[i]

ans = 0
for i in range(n):
    # print("{}について".format(a[i]))
    # print("初項:{} 公差:{}なので".format(first_subarr[i], diffs[i]))
    tmp = k * (2 * first_subarr[i] + (k - 1) * diffs[i]) // 2
    # print("総和は{}".format(tmp))
    ans += tmp
    ans %= MOD
print(ans)