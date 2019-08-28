# ソートして全探索
# -> 調和級数たらいうんちゃうんかこれオイ


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(sorted(input())))

c = 0
for i in range(n - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        if arr[i] == arr[j]:
            c += 1

print(c)
