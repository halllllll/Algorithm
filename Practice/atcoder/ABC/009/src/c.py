n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(list(set(arr)))
print(arr[-2])
