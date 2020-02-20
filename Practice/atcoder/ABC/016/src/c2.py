# さっきは再帰で解いたけどループのほうが楽では
n, m = map(int, input().split())
table = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    table[a - 1].append(b - 1)
    table[b - 1].append(a - 1)

for i in range(n):
    ans = []
    for j in table[i]:
        for k in table[j]:
            if i != k and k not in table[i]:
                ans.append(k)
    print(len(set(ans)))
