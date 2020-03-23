# 1って書かれたM個と2って書かれたN個があるよって感じのncr
# 「N+M個のうちM個のうち2個」だとわけがわからんので別の方法を考える。
# 全体から奇数になるやつを引けばいいかもしれない ncr(N+M,2)-ncr(N, 1)-ncr(M, 1) = ncr(N+M, 2)-(N*M)

n, m = map(int, input().split())


def ncr(n, r):
    res = 1
    for i in range(1, r + 1):
        res = res * (n - i + 1) // i
    return res


print(ncr(n + m, 2) - n * m)
