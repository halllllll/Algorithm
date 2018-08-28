while True:
    h, w = map(int, input().split())
    if w+h == 0:
        break
    line = "#"*w
    for y in range(h):
        print(line)
    print()
