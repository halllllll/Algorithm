# N<=100000なので愚直にインクリメントしていった最初のやつでいいんじゃないかと思い始めた 繰り上がりとかの場合分けがめんどいし
n, k = map(int, input().split())
nglist = list(input().split())
while True:
    strn = str(n)
    flag = True
    for ng in nglist:
        if ng in strn:
            flag = False
            break
    if flag:
        break
    else:
        n += 1
print(n)
