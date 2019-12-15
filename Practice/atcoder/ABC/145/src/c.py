import itertools

n = int(input())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

perm = list(itertools.permutations(list(range(n))))
m = len(perm)
ans = 0
for p in perm:
    tmp = 0
    limit = len(p)
    for pi in range(limit - 1):
        a = (table[p[pi]][0] - table[p[pi + 1]][0]) ** 2
        b = (table[p[pi]][1] - table[p[pi + 1]][1]) ** 2
        g = (a + b) ** 0.5
        tmp += g
    ans += tmp

print(ans / m)

