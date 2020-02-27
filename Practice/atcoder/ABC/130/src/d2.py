# 尺取の練習と聞いて
n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
r = 0
tmp_sum = 0
for l in range(n):
    # 条件を満たすまで右端を伸ばす
    while r < n and tmp_sum < k:
        tmp_sum += arr[r]
        r += 1
    # whileを抜けた時は条件を満たしている
    if r == n:
        while tmp_sum >= k and l <= n:
            tmp_sum -= arr[l]
            ans += 1
            l += 1
        break
    else:
        ans += n - r + 1
        tmp_sum -= arr[l]

print(ans)

