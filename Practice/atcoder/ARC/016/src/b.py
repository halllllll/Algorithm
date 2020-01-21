# 横は関係ないので縦*10でみていけばいいね
n = int(input())
score = [[] for _ in range(9)]
for _ in range(n):
    line = list(input())
    for i in range(9):
        score[i].append(line[i])

# 面倒なので番兵を置く あれ？実質番兵法の練習じゃねこれ
for _ in range(n):
    for i in range(9):
        score[i].append("-")

ans = 0
for i in range(9):
    t = 0
    while t < n:
        if score[i][t] == "x":
            ans += 1
            t += 1
        elif score[i][t] == ".":
            t += 1
            continue
        elif score[i][t] == "o":
            while score[i][t] == "o":
                t += 1
            ans += 1
        else:
            # 不可侵領域
            print(1 / 0)
print(ans)
