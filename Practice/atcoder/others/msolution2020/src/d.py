# 決め打ちすることを考える。i=0をS/Wとしても、結局i=1が分からないので先に進めない。なのでi=1も決め打ちする。
# すべてのiを決め打ちする必要はなく、これだけ決めればあとは決まっていく。
# したがって初期状態は4通り

n = int(input())
s = list(input())


def f(pattern):
    for i in range(1, n):
        if pattern[-1] == "S":
            if s[i] == "o":
                # ひとつ前と一緒
                pattern.append(pattern[-2])
            else:
                pattern.append("S" if pattern[-2] == "W" else "W")
        else:
            if s[i] == "o":
                # ひとつ前と別
                pattern.append("S" if pattern[-2] == "W" else "W")
            else:
                pattern.append(pattern[-2])
    return pattern


for p in [["S", "S"], ["S", "W"], ["W", "W"], ["W", "S"]]:
    ret = f(p[:])
    print(ret)
    # if ret[-1] == ret[0]:
    #     print("".join(ret[:n]))
    #     # exit()
print(-1)