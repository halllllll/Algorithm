a, b, m = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
ans = min(arr) + min(brr)
for _ in range(m):
    x, y, c = map(int, input().split())
    ans = min(ans, arr[x - 1] + brr[y - 1] - c)
print(ans)
