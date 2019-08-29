# 移動するのすらコストかかるのがアホらしいので、着いたらギリギリまで粘ることにする
# 「そこに至るまでの最短コスト」を取れば復路も最適になるのでBFSでいく

from collections import deque

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
  gets = list(map(int, input().split()))
  graph[gets[0]].append([gets[1], gets[2]]) # [from] = [to, cost]

P = [False for _ in range(N)]

queue = deque()
queue.append()

while not all(P) or len(q)>0:
  q = queue.popleft()
