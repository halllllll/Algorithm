a = list(map(int, input().split()))
# 1個
if a[0] == a[1] + a[2] + a[3] or a[1] == a[0] + a[2] + a[3] or a[
        2] == a[0] + a[1] + a[3] or a[3] == a[0] + a[1] + a[2]:
    print("Yes")
elif a[0] + a[1] == a[2] + a[3] or a[0] + a[2] == a[1] + a[3] or a[0] + a[
        3] == a[1] + a[2]:
    print("Yes")
else:
    print("No")