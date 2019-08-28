# 隣接リストでBFS
# 色分け。
# 色分け、逐次やるんじゃなくて、生成していく。
# しかも「最初は互いに素にして仲間を増やしていく」じゃなくて、
# 「どこの色にも属していないところから仲間を増やしていく」というスタンス
# こうしない場合（互いに素から始める場合）の実装ができなかった

n, m = map(int, input().split())
colors = [0 for _ in range(n)]  # 0がどこにも属していない状態ということにする
graph = [[] for _ in range(n)]
for _ in range(m):
    s, t = map(int, input().split())
    graph[s].append(t)
    graph[t].append(s)  # これを忘れていた...

# 先に色分けする これで探索はO(1)
color = 1
for i in range(n):
    stack = [i]
    if colors[i] == 0:
        colors[i] = color
    while len(stack) > 0:
        nexi = stack.pop()
        for ni in graph[nexi]:
            if colors[ni] == 0:
                colors[ni] = color
                stack.append(ni)
    color += 1

for i in range(int(input())):
    s, t = map(int, input().split())
    if colors[s] == colors[t]:
        print("yes")
    else:
        print("no")
