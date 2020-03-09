# Nが小さいので全探索の構え -> なにをどうする？
# A,B,Cしかないので「li本目をA,B,Cどれの材料にするか」でやれそう -> 振り分けてから和をとって（+=10）それぞれの差を計算(+=1)
n, a, b, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))


def rec(i, ai, bi, ci):
    if i == n:
        if ai == 0 or bi == 0 or ci == 0:
            # 各最低でも1本以上必要だよね
            return 10 ** 10
        return abs(a - ai) + abs(b - bi) + abs(c - ci)
    else:
        ret = 10 ** 10
        # いま注目してるやつをa,b,cどれに属することにするか選ぶ
        if ai == 0:
            ret = min(ret, rec(i + 1, arr[i], bi, ci))
        elif ai > 0:
            ret = min(ret, rec(i + 1, ai + arr[i], bi, ci) + 10)
        if bi == 0:
            ret = min(ret, rec(i + 1, ai, arr[i], ci))
        elif bi > 0:
            ret = min(ret, rec(i + 1, ai, bi + arr[i], ci) + 10)
        if ci == 0:
            ret = min(ret, rec(i + 1, ai, bi, arr[i]))
        elif ci > 0:
            ret = min(ret, rec(i + 1, ai, bi, ci + arr[i]) + 10)
        # 今回は選ばない場合もある
        ret = min(ret, rec(i + 1, ai, bi, ci))
        return ret


print(rec(0, 0, 0, 0))
