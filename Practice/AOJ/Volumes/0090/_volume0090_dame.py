# それぞれのシールについて他のシールとの差を計測していけばO(N^2)で終わるっしょ 円形だし中心座標と半径だけ考えればいいね
# と思ったらそれじゃ「i番目のシールはi自身を含めて何枚のシールと重なっているか」になってしまう
# (重なっている部分、がわからない)


while True:
    n = int(input())
    if n == 0:
        break
    x, y = [], []
    for _ in range(n):
        xv, yv = map(float, input().split(","))
        x.append(xv)
        y.append(yv)
    ans = 1

    for i in range(n):
        tmp = 1
        for j in range(n):
            if i == j:
                continue
            length = (pow(x[i] - x[j], 2) + pow(y[i] - y[j], 2)) ** 0.5
            if 2 >= length:
                tmp += 1
        ans = max(ans, tmp)

    print(ans)
