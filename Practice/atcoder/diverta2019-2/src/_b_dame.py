# y = ax + b上に最も多く等間隔で並ぶもの以外にコストを支払う
# 適当に２つ選んだとき、残ったものがいくつその条件を満たすかを数え、最も多いものを採用

# とか考えたけど実装できず 解答を見る
# ケチケチせずに果敢にN^4で全探索するらしい

# でやったのにWAなる わけわからん

n = int(input())
xs, ys = [], []
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
max_count = -1
for i in range(n):
    for j in range(i, n):
        if i == j or xs[i] == xs[j]:
            continue
        # 差はi-jとする
        p, q = xs[i] - xs[j], ys[i] - ys[j]
        # print("p, q = {} {}".format(p, q))
        count = 0
        # ここから全探索
        for k in range(n):
            for l in range(n):
                if p == xs[k] - xs[l] and q == ys[k] - ys[l]:
                    # print("yay!!")
                    count += 1
        # print("count result = {}".format(count))
        max_count = max(max_count, count)
print(max(1, n - max_count))

