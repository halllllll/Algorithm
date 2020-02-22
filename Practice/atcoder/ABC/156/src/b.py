n, k = input().split()


def base_10_to_n(X, n):
    if int(X / n):
        return base_10_to_n(int(X / n), n) + str(X % n)
    return str(X % n)


x = base_10_to_n(int(n), int(k))
print(len(x))
