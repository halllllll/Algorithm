# 辺の情報を別で管理しておけば、辺を取り除いたときの状態でシミュレートできる
# 隣接リストじゃなくて隣接行列でもっておく
# 適当にDFSして訪れられなかった場合に+1
n, m = map(int, input().split())
grpah = [[False for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    grpah[a - 1][b - 1] = True
    grpah[b - 1][a - 1] = True


def dfs(cur, visited):
    if all(visited) is False and all(grpah[cur]) is False:
        for i, v in enumerate(grpah[cur]):
            if v == True and visited[i] == False:
                visited[i] = True
                dfs(i, visited)


ans = 0

for i in range(n):
    for j in range(n):
        if grpah[i][j] or grpah[j][i]:
            # 辺を一時的に取り除く
            grpah[i][j] = grpah[j][i] = False
            temp_visited = [False for _ in range(n)]
            temp_visited[0] = True
            dfs(0, temp_visited)
            if all(temp_visited) is False:
                ans += 1

            # 取り除いた辺を復元しておく
            grpah[i][j] = grpah[j][i] = True

print(ans//2)
