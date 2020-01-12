n, k, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = (m * n) - sum(arr)
print(max(0, ans) if ans <= k else -1)
