# a<=b<=cとしてc-aとc-bの差が偶数なら2で割ればいいし奇数ならceil+1
a, b, c = sorted(list(map(int, input().split())))
if (c - a + c - b) % 2 == 0:
    print((c - a + c - b) // 2)
else:
    print((c - a + c - b) // 2 + 2)
