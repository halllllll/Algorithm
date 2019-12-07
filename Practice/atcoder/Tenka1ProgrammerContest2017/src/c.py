# おなじみ 1/w = ...の形からもっていくとw = ..が導出できた

N = int(input())
for n in range(1, 3501):
    for h in range(1, 3501):
        t = 4 * n * h - N * (h + n)
        if t == 0 or t < 0:
            continue
        w = (N * n * h) / t
        if int(w) == w:
            w = int(w)
            print(h, n, w)
            exit()
