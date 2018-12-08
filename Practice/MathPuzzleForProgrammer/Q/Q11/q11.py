a, b = 1, 1
c = 0
while True:
    if c >= 5:
        break
    a, b, ab = b, a + b, a + b
    s = 0
    if b <= 144:
        continue
    while True:
        if ab == 0:
            break
        s += ab % 10
        ab //= 10
    if b % s == 0:
        c += 1
        print(b)
