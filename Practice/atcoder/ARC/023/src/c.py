# a -1 b とかのときは-1はa以上b以下のいずれか。a -1 -1 b とかだと
# 2 -1 -1 5 -> [2 2 2 5] [2 2 3 5] [2 2 4 5] [2 2 5 5](4) [2 3 3 5] [2 3 4 5] [2 3 5 5](3) [2 4 4 5] [2 4 5 5](2) [2 5 5 5](1)
# おわかりいただけただろうか
n = int(input())
arr = list(map(int, input().split()))
MOD = 10 ** 9 + 7
ans = 0

i = 0

while i < n:
    if arr[i] == -1:
        a = i - 1
        i += 1
        while i < n and arr[i] == -1:
            i += 1
        b = i
        # ふつうにsum(list)だと間に合わんので等差数列の和を使う
        ans += (arr[a] + arr[b] - 1) * (arr[b] - arr[a]) // 2
        ans %= MOD
    else:
        i += 1
print(ans)

