from collections import deque
n, m = map(int, input().split())
table = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    table[a].append(b)
    table[b].append(a)

ans = [0] * (n + 1)
ans[1] = -1
queue = deque()
for s in table[1]:
    ans[s] = 1
    # 注目してるノード番号, ひとつ前の番号
    queue.append((s, 1))
while len(queue) > 0:
    node = queue.popleft()
    for t in table[node[0]]:
        if ans[t] != 0 or t == 0:
            continue
        ans[t] = node[0]
        queue.append((t, node[0]))
if 0 in ans[2:]:
    print("No")
else:
    print("Yes")
    for a in ans[2:]:
        print(a)
