n = int(input())
arr = [[i + 1, int(v)] for i, v in enumerate(input().split())]
sorted_arr = list(map(lambda x: str(x[0]), sorted(arr, key=lambda x: x[1])))

print(" ".join(sorted_arr))
