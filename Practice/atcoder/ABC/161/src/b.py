n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = sum(arr)
if arr[n - m] >= s / (4 * m):
    print("Yes")
else:
    print("No")
