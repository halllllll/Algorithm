# 二回訪れたら終了、それまでに2に行ったらOK
# インデックスと値を入れ替えながらやってみる
n = int(input())
dic = []
for i in range(n):
    dic.append(int(input()))

used = [False for _ in range(10 ** 5 + 1)]
tmp = 1
ans = 0
while True:
    target = dic[tmp - 1]
    if target == 2:
        print(ans + 1)  # 次の一手で決まるので
        exit()
    if used[target]:
        print(-1)
        exit()
    tmp = target
    used[tmp] = True
    ans += 1
