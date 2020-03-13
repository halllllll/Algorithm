# サンプル1はべつに3*2=6じゃなくても4*2=8（[1 3 4][2 2 4]）や5*1=10（[1 4 5]）も同じコストで実現できることがわかる
# つまり総和に近い偶数を目指す
n = int(input())
arr = list(map(int, input().split()))
s = sum(arr)
tmp = arr[0]
ans = 10**10
e = -1
for i in range(1, n):
    # 超えないギリギリ
    if tmp + arr[i] <= s // 2:
        tmp += arr[i]
        e = i
    else:
        break
c = abs(s // 2 - tmp) + abs(s // 2 - sum(arr[i:]))
# print("超えない左側の合計と右側の合計 : {}, {}".format(tmp, sum(arr[i:])))
ans = min(ans, c)

e = -1
tmp = arr[0]
for i in range(1, n):
    # 超えたギリギリ
    if tmp > s // 2:
        break
    else:
        tmp += arr[i]
        e = i
c = abs(s // 2 - tmp) + abs(s // 2 - sum(arr[i:]))
# print("超えたギリギリの左側の合計と右側の合計 : {}, {}".format(tmp, sum(arr[i:])))
ans = min(ans, c)
print(ans)