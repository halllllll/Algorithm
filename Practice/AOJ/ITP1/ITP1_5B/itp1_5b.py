while True:
    h, w = map(int, input().split())
    if w+h == 0:
        break
    line = ""
    for y in range(h):
        if y == 0 or y == h-1:
            line = "#"*w
        else:
            line = "#"+"."*(w-2)+"#"
        print(line)
    print()
