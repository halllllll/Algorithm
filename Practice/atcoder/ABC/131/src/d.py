# 締切が近い順に処理する（締め切り時間が同じならかける時間の順番は関係ない）

n = int(input())

# こういう処理pythonでうまくやる方法ないのかな ...
hash = {}
for _ in range(n):
    a, b = map(int, input().split())
    if b in hash:
        hash[b].append(a)
    else:
        hash[b] = [a]
arr = []
for k, v in hash.items():
    arr.append([k, v])
arr = list(sorted(arr, key=lambda x: x[0]))

count = 0
for a in arr:
    for ai in a[1]:
        if count + ai > a[0]:
            print("No")
            exit()
        else:
            count += ai
print("Yes")
