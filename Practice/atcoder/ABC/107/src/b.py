H, W = map(int, input().split())
m = [list(map(str, input().split())) for i in range(H)]

print(m)


def check(m):
    print("m[0]: {}".format(m[0]))
    nw, nh = len(m[0]), len(m)
    print("nw: {}, nh: {}".format(nw, nh))
    nm = []
    # とりあえず横
    for _, w in enumerate(m):
        if all([x == '.' for x in w]):
            print("なんかする")
            break
        else:
            nm.add(w)

    print(nm)


check(m)
