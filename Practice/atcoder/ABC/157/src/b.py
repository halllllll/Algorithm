bingo = []
for i in range(3):
    bingo.append(list(map(int, input().split())))

n = int(input())
for _ in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if bingo[i][j] == b:
                bingo[i][j] = "o"

for i in range(3):
    flag = 0
    for j in range(3):
        if bingo[i][j] == "o":
            flag += 1
    if flag == 3:
        print("Yes")
        exit()
    flag = 0
    for j in range(3):
        if bingo[j][i] == "o":
            flag += 1
    if flag == 3:
        print("Yes")
        exit()
# 斜め
if (
    bingo[0][0] == bingo[1][1] == bingo[2][2] == "o"
    or bingo[0][2] == bingo[1][1] == bingo[2][0] == "o"
):
    print("Yes")
    exit()
print("No")
