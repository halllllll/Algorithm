# どうせ何を喰っても自分のポイントは入るので、
# 高橋くんは青木くんの得られるポイントの最大のやつを,青木くんは高橋くんのvice versa
n = int(input())
arr = []
used = [False for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    arr.append([i, a, b])

tak = sorted(arr, key=lambda x: x[1], reverse=True)
aok = sorted(arr, key=lambda x: x[2], reverse=True)
takp, aokp = 0, 0
# 毎回どのインデックスを使ってないかを調べるとTLEなるので、
# どうせソート済みを利用してインデックス参照して次に喰う料理のインデックスを探す
c = 0
taki, aoki = (0, 0)
while c < n:
    if c % 2 == 0:
        # 高橋くんのターン
        while used[aoki]:
            aoki += 1
        used[aok[aoki][0]] = True
        takp += aok[aoki][1]  # 青木くんの得られるポイントで降順ソートしたインデックスの料理を食べた時に得られる高橋くんのポイント
    else:
        # 青木くんのターン
        while used[taki]:
            taki += 1
        used[tak[taki][1]] = True
        aokp += tak[taki][2]  # 略
    c += 1

print(takp - aokp)
