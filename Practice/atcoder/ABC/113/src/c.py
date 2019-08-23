# 見かけたのでやる
# やるだけ
# インプットの順番をidで保存しておいてyでソートしてpでソートしてidでソートして復元
n, m = map(int, input().split())
arr = []
for i in range(m):
    p, y = map(int, input().split())
    arr.append([i, p, y])

arr = list(sorted(arr, key=lambda x: x[2]))
arr = list(sorted(arr, key=lambda x: x[1]))
# print(arr)
flag = -1
count = 1
for a in arr:
    if a[1] != flag:
        flag = a[1]
        count = 1
    a[2] = "%06d" % count
    a[1] = "%06d" % a[1]
    count += 1
arr = list(sorted(arr, key=lambda x: x[0]))
for a in arr:
    print("{}{}".format(a[1], a[2]))

