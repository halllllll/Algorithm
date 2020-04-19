# めんどいな DFS
n = int(input())
bukas = [[] for _ in range(n)]
for i in range(n - 1):
    b = int(input())
    bukas[b - 1].append(i + 1)

used = [False for _ in range(n)]
used[0] = True


def dfs(i):
    sarallies = []
    for b in bukas[i]:
        if used[b] == False:
            sarallies.append(dfs(b))
            used[b] = True
    return 1 if len(sarallies) == 0 else max(sarallies) + min(sarallies) + 1


print(dfs(0))