# よくよく考えたら最短距離がほしい+経路がほしいのでBFSとDFSでそれぞれいけるんじゃないか
from collections import deque
n = int(input())
a, b = map(int, input().split())
m = int(input())
table = [[] for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    table[x - 1].append(y - 1)
    table[y - 1].append(x - 1)

queue = deque()
queue.append((a - 1, 0))
dist = -1
passed = [False for _ in range(n)]
passed[a - 1] = True
while len(queue) > 0:
    cur = queue.popleft()
    if cur[0] == b - 1:
        dist = cur[1]
        break
    for i in table[cur[0]]:
        if passed[i] == False:
            passed[i] = True
            queue.append((i, cur[1] + 1))

dp = {}
passed = [False for _ in range(n)]
passed[a - 1] = True


def dfs(i, cur, passed):
    if (i, cur) in dp:
        return dp[(i, cur)]
    if cur > dist:
        return 0
    if i == b - 1 and cur == dist:
        return 1
    ret = 0
    for next_node in table[i]:
        if passed[next_node] == False:
            passed[next_node] = True
            ret += dfs(next_node, cur + 1, passed)
            ret %= 10**9 + 7
            passed[next_node] = False
    dp[(i, cur)] = ret
    return ret


print(dfs(a - 1, 0, passed))
