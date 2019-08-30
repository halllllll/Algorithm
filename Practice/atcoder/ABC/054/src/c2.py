# 全域木？っていうんだっけ？でもコストは関係ないか
# 適当に隣接リストでもってしてDFSする
N, M = map(int, input().split())
Neighbor_list = [[] for _ in range(N)]
for _ in range(M):
    s, t = map(int, input().split())
    Neighbor_list[s-1].append(t-1)
    Neighbor_list[t-1].append(s-1)


def dfs(cur, path):
    if len(path) == N:
        return 1
    else:
        ret = 0
        for neighbor in Neighbor_list[cur]:
            if neighbor not in path:
                next_list = path[:]
                next_list.append(neighbor)
                ret += dfs(neighbor, next_list)
        return ret


print(dfs(0, [0]))
