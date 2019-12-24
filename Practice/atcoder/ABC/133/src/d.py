# (d1+d2)/2 == n1, (d2+d3)/2 == n2... が矛盾なくなるようにする
# にぶたんを使う
# rを10**9にしてたらなんかしらんけど駄目だった 10にしたらいけた...

# なんか偶数のための配列の取り扱いがクソわからんので1..5を2..10に拡張するなどするようなmidの取り方をした

n = int(input())
dum = list(map(int, input().split()))
l, r = 0, (10 ** 10) // 2

while True:
    mid = (l + r) // 2
    rain = [0 for _ in range(n)]
    rain[0] += mid * 2
    for i in range(1, n):
        next_amount = (dum[i - 1] - (rain[i - 1] // 2)) * 2
        rain[i] += next_amount

    if dum[-1] == (rain[-1] + rain[0]) // 2:
        rain = list(map(str, rain))
        print(" ".join(rain))
        exit()
    if (rain[0] + rain[-1]) // 2 < dum[-1]:
        l = mid + 1
    else:
        r = mid


"""
7
110 50 53 50 11 36 88

11
38 7 15 15 9 31 23 1 5 55 81
"""
