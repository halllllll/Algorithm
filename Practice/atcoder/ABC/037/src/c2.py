# 累積和して範囲内の最大から範囲外のうち範囲外の最小より大きい値を引く
n, k = map(int, input().split())
arr = list(map(int, input().split()))
ruiseki_arr = [0 for _ in range(n+1)]
ruiseki_arr[1] = arr[0]
for i in range(1, n+1):
    ruiseki_arr[i] = arr[i-1] + ruiseki_arr[i-1]
ans = 0
for i in range(k, n+1):
    ans += ruiseki_arr[i] - ruiseki_arr[i - k]

print(ans)
