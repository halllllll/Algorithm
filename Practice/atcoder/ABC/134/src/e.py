n = int(input())
arr = [int(input()) for _ in range(n)]
max_arr = [0 for _ in range(n)]
max_arr[0] = arr[-1]
for i, a in enumerate(arr[-2::-1]):
    if max_arr[i] < a:
        max_arr[i + 1] = a
    else:
        max_arr[i + 1] = max_arr[i]

max_arr = max_arr[::-1]
print(arr)
print(max_arr)
