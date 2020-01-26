h, n = map(int, input().split())
arr = sorted(map(int, input().split()))
if h <= sum(arr):
    print("Yes")
else:
    print("No")

