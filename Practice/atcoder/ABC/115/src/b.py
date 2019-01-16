n = int(input())
arr = []
for _ in range(n):
    x = int(input())
    arr.append(x)

arr = sorted(arr)
print(int(arr[-1]/2) + sum(arr[:-1]))
