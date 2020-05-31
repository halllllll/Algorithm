# だっる pythonだと空文字もlistすりゃいいんだっけ？ すぐ忘れそう
n, l = map(int, input().split())
table = []
for ll in range(l):
    table.append(list(input()))
table = table[::-1]
cur = list(input()).index('o')
for i in range(l):
    if n == 1:
        continue
    if cur == 0:
        if table[i][cur + 1] == "-":
            cur += 2
    elif cur == n + n - 2:  # 最悪
        if table[i][cur - 1] == "-":
            cur -= 2
    elif table[i][cur + 1] == "-":
        cur += 2
    elif table[i][cur - 1] == "-":
        cur -= 2
print(cur // 2 + 1)
