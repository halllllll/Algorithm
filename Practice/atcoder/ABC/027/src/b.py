# 全体の人数を島の数で割り切れる場合のみ可能
# 少なくても多くても隣の島に橋をかけなくてはならないのでそうする
# いやよく考えたら累積しながらで判断できるか

n = int(input())
arr = list(map(int, input().split()))
if sum(arr) % n != 0:
    print(-1)
    exit()
if sum(arr) == 0:
    print(0)
    exit()

divider = sum(arr) // n
ans = 0
cur = 0
for i in range(n):
    cur += arr[i]
    if cur != (i + 1) * divider:
        ans += 1

print(ans)
