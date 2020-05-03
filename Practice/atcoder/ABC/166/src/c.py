n, m = map(int, input().split())
h = list(map(int, input().split()))

table = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    table[a].append(b)
    table[b].append(a)

ans = set()
for i in range(n):
    stack = table[i]
    highest = h[i]
    flag = True
    for t in table[i]:
        if highest <= h[t]:
            flag = False
            break
    if flag:
        ans.add(i)
print(len(ans))
