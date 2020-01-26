# わからんので解説を読んだがよくわからん
# とりあえずaから各ノードへの最短距離を出して、それをもとにDPするらしい
# ん？でも最短距離の数を更新しながらBFSできるんじゃね？
# なぜか実装できない（あたまがわるい わるすぎる）

# print使いまくってデバッグしまくった
# 満を持して提出するもWAWAWAWAWAWAWAWAWAWAWA~~~WAWAWA~~~~

from collections import deque

n = int(input())
a, b = map(lambda x: int(x) - 1, input().split())
m = int(input())
table = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    table[x].append(y)
    table[y].append(x)

# minpath[i] = aからiに向かう最短距離
min_path = [10 ** 10 for _ in range(n)]
min_path[a] = 0

# cnt[i] = aからiに向かう最短距離の数
cnt = [0 for _ in range(n)]
cnt[a] = 1

# bfsでaからほかの全点への最短距離をアレする bfsでたどり着く場所はそのマスへの最短距離なので。
arr = deque()
arr.append(0)
while len(arr) > 0:
    cur = arr.popleft()
    for next_node in table[cur]:
        # print("next_node {}".format(next_node))
        if min_path[next_node] < 10 ** 10:
            # すでに到達済み
            if min_path[cur] + 1 == min_path[next_node]:
                # print("条件を満たしたので最短距離加算")
                cnt[next_node] += cnt[cur]
                cnt[next_node] %= 10 ** 9 + 7
                # print("加算後 {}".format(cnt))
            continue
        # まだ到達してない
        # print("はじめて{}についたよ".format(next_node))
        cnt[next_node] = cnt[cur]
        min_path[next_node] = min_path[cur] + 1
        arr.append(next_node)
        # print("now min path : {}".format(min_path))
        # print("now cnt : {}".format(cnt))
# print(table)
# print(min_path)
# print(cnt)
print(cnt[b])
