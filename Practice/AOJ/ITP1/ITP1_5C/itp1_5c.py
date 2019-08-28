while True:
    h, w = map(int, input().split())
    if w+h == 0:
        break
    for y in range(h):
        line = ""
        for x in range(w):
            if (y+x) % 2 == 0:
                line += "#"
            else:
                line += "."
        print(line)
    print()
