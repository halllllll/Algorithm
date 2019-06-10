# eval is evil
S = input()


def f(i, c):
    # i番目まで / 現在の式
    if i == len(S):
        if c[-1] == "+":
            return int(eval(c[:-1]))
        else:
            return int(eval(c))
    # i番目で区切る or 区切らない ただし+は連続しない
    if i == 0 or c[-1] == "+":
        return f(i + 1, c + S[i])
    else:
        return f(i, c + "+") + f(i + 1, c + S[i])


print(f(0, ""))
