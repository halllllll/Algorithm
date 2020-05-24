# 愚直解を書いたはずなのになぜかgolangでWAを食らうのでキレてpythonで同じことをしてみるテスト

N, R = map(int, input().split())
s = input()
rest = s.count(".")
INF = 10**8
dp = {}
if R == 1:
    print(s.rfind(".") + rest)
    exit()
s = list(s)


def rec(l, i, r, level):
    if (i, r) in dp:
        return dp[(i, r)]
    # print(f"now l {' '*level}{l}")
    if i == N or N - i < r:
        # print("無理では")
        return INF
    if r == 0:
        # print("殲滅完了")
        return 0
    t = l[:]
    hit = 0
    for j in range(i, min(N, i + R)):
        if l[j] == ".":
            hit += 1
            t[j] = "o"
    ret = INF
    if hit == 0:
        ret = min(ret, rec(l, i + 1, r, level + 1) + 1)
    else:
        ret = min(ret, rec(t, i, r - hit, level + 1),
                  rec(l, i + 1, r, level + 1)) + 1
    dp[(i, r)] = ret
    return ret


print(rec(s, 0, rest, 0))