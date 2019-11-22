D = {"A": input(), "B": input(), "C": input()}


def f(t):
    if len(D[t]) == 0:
        print(t)
        exit()
    next_t = D[t][0]
    D[t] = D[t][1:]
    f(next_t.upper())

f("A")
