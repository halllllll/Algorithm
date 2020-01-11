# どうせN=8なので探索
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

def f(n, cur=[]):
    if len(cur) == n:
        yield cur
    else:
        for i in range(1, n + 1):
            if i not in cur:
                _next = cur[:]
                _next.append(i)
                yield from f(n, _next)


idx = 1
pflag, qflag = False, False
for g in f(n):
    if p == g:
        pflag = idx
    if q == g:
        qflag = idx
    if pflag and qflag:
        break
    idx += 1
print(abs(pflag - qflag))
