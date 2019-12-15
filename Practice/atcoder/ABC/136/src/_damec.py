# 単調非減少の意味は知らんが、sample2を見る限り、全部高さはダメなのだろう
# 最初と最後が1か、単調減少だと実現不可能
# ん？ということは最後が1以外は全部可能？

# -> ダメでした
# よく呼んだら1度ずつって書いてあるしアホだった 二回回す
# ダメだった 3回回す
# ->ダメでした

n = int(input())
arr = list(map(int, input().split()))
used = [False for _ in range(n + 1)]
arr.insert(0, arr[0])
for i in range(1, n + 1):
    if arr[i] < arr[i - 1]:
        arr[i - 1] -= 1
        used[i - 1] = True

for i in range(1, n):
    if arr[i + 1] < arr[i]:
        if used[i] != True:
            arr[i] -= 1
            used[i] = True

for i in range(1, n):
    if arr[i + 1] < arr[i]:
        print("No")
        exit()

print("Yes")
