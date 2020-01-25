# とき直し
# ふつうに全探索でいいや
t = int(input())
n = int(input())
# tako
a = list(map(int, input().split()))
m = int(input())
# kyaku
b = list(map(int, input().split()))
used_tako = [False for _ in range(n)]

for i in range(m):
    ok = False
    for j in range(n):
        if used_tako[j] == False and a[j] <= b[i] <= a[j] + t:
            used_tako[j] = True
            ok = True
            break
    if ok == False:
        print("no")
        exit()
print("yes")
