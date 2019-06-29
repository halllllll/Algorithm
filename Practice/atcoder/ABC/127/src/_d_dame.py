# ソートしたやつを小さいやつから書き換えたら嬉しいが、書き換えた結果小さくならないようにする
# bを何枚まで選ぶかはにぶたんで、比較は予め累積和をとっておいたもので
# 配列、更新していくってのを誤読して数分溶かした（それぞれのうちいずれかを取ったときの最大かと思ってた）
# とやったらTLEなった

n, m = map(int, input().split())
arr = list(sorted(list(map(int, input().split()))))
ruiseki = [0 for _ in range(n+1)]
for i in range(1, n+1):
    ruiseki[i] = ruiseki[i-1] + arr[i-1]

for i in range(m):
    b, c = map(int, input().split())
    l, r = 0, b
    while l < r:
        mid = (l + r) // 2
        if arr[mid] > c:
            r = mid
        else:
            l = mid + 1

    # rまで書き換えていい
    # print("vs: {} sum={}".format([c] * r + arr[r:], sum([c] * r + arr[r:])))
    arr = list(sorted([c] * r + arr[r:]))

print(sum(arr))
