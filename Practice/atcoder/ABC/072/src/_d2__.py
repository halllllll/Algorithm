# 前回アタックしたのはいつかは知らんし問題すら憶えてない
# i==Aiの数を調べ、あとからとなりあってる数を引く
# （こんな雑なのでいいのかな....)
# WAだったので退化してますね 死んだほうがいいね
n = int(input())
arr = list(map(int, input().split()))
ans = 0
pair = 0
for i in range(1, n + 1):
    if i == arr[i - 1]:
        ans += 1
for i in range(n - 1):
    if i + 1 == arr[i] and i + 2 == arr[i + 1]:
        pair += 1
print(ans - pair)
