# 典型ナップザックと思うと解けない（配列がとんでもないことになる）
# 制約から考えると重さは4種類で合計最大100個なので「どの重さがいくつあるか」で探索できる

n, w = map(int, input().split())
weight = {}
first = list(map(int, input().split()))
for i in range(first[0], first[0] + 4):
    weight[i] = []
weight[first[0]].append(first[1])
for _ in range(n - 1):
    w, v = map(int, input().split())
    weight[w].append(v)


weight = dict([[k, sorted(v, reverse=True)] for k, v in weight.items()])
keys = list(weight.keys())

ans = 0
for i in range(len(weight[keys[0]])):
    for j in range(len(weight[keys[1]])):
        for k in range(len(weight[keys[2]])):
            for l in range(len(weight[keys[3]])):
                if i * keys[0] + j * keys[1] + k * keys[2] + j * keys[3] <= w:
                    ans = max(
                        ans,
                        weight[keys[0]][:i]
                        + weight[keys[1]][:j]
                        + weight[keys[2][:k]]
                        + weight[3][:l],
                    )

print(ans)
