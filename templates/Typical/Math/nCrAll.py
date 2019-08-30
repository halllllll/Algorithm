def nCr(i, cur, rest, target):
    if rest == 0:
        yield cur
    elif len(target) - i == rest:
        # 今回のやつを取るしかない
        nex = cur[:]
        nex.append(target[i])
        for ncr in nCr(i+1, nex, rest-1, target):
            yield ncr
    else:
        # 含めるか含めないか
        nex = cur[:]
        nex.append(target[i])
        for ncr in nCr(i+1, nex, rest-1, target):
            yield ncr
        for ncr in nCr(i+1, cur[:], rest, target):
            yield ncr


arr = list(range(8))
g = nCr(0, [], 5, arr)
for x in g:
    print(x)
