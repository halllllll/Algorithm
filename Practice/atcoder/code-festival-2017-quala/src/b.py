# 横の回数をx, 縦の回数をyとすると k=x*(M-2)+y*(N-2)になればいい
# あとは例外 N or M==1のときはK<=N*Mからすべての値が可能
# N or M==2のときはすべての偶数が可能
# KがNorMで割り切れれば可能
n, m, k = map(int, input().split())
if n == 1 or m == 1:
    print("Yes")
    exit()
if (n == 2 or m == 2) and k % 2 == 0:
    print("Yes")
    exit()
if k % n == 0 or k % m == 0:
    print("Yes")
    exit()
for y in range(1, n):
    for x in range(1, m):
        # print("y, x = {}, {}".format(y, x))
        # print("面積 {}".format((y * m - x * y) + x * (n - y)))
        if k == (y * m - x * y) + x * (n - y):
            # print(y, x)
            # print("y*x={}".format(y * x))
            print("Yes")
            exit()
print("No")
