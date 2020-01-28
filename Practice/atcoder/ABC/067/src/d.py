# [数学、特にグラフ理論の分野における木（き、）とは、連結で閉路を持たないグラフである。]
# なので1->Nは1通り。つまり1->Nの最短経路上にあるマスをつぶすのが先
# で、残ったのを探索できるが、こういう二段構えで実装するのが面倒。
# もうちょっと考えると、1->i とi->Nの距離をみたとき、前者が小さければ先に到達できるので黒で埋められることが分かる
# （進めなくなったら負け、がめんどくさいが、すすめなくなったらパス、とすると、勝敗は変わらないことになる）
# 1とNからスタートして2回BFSすりゃいいか

import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)

table_from_one = [10 ** 5 for _ in range(n)]
table_from_one[0] = 0
table_from_n = [10 ** 5 for _ in range(n)]
table_from_n[-1] = 0
arr_from_one = deque([0])
arr_from_n = deque([n - 1])


def set_table(table, arr):
    while len(arr) > 0:
        cur = arr.popleft()
        for next_node in graph[cur]:
            if table[next_node] < 10 ** 5:
                continue
            table[next_node] = table[cur] + 1
            arr.append(next_node)


set_table(table_from_one, arr_from_one)
set_table(table_from_n, arr_from_n)
result = 0
for i in range(n):
    if table_from_one[i] <= table_from_n[i]:
        result += 1
    else:
        result -= 1
print("Fennec" if result > 0 else "Snuke")
