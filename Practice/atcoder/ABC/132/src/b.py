n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in range(1, n - 1):
    if arr[i - 1] < arr[i] < arr[i + 1] or arr[i - 1] > arr[i] > arr[i + 1]:
        count += 1

print(count)
