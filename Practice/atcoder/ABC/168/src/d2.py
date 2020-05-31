# BFSして終わり 必ず存在するので
from collections import deque

n, m = map(int, input().split())
t = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    t[a].append(b)
    t[b].append(a)

stamp = [0] * (n + 1)
stamp[0], stamp[1] = -1, -1
queue = deque()
for tv in t[1]:
    queue.append((tv, 1))
    stamp[tv] = 1

while len(queue) > 0:
    cur_node, pre_node = queue.popleft()
    for nex_node in t[cur_node]:
        if stamp[nex_node] != 0:
            continue
        stamp[nex_node] = cur_node
        queue.append((nex_node, pre_node + 1))

print("Yes")
for i in stamp[2:]:
    print(i)