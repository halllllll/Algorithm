# 九九の合計が問題文から予想できるので流用する やるだけ
n = int(input())
target = 2025 - n
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == target:
            print("{} x {}".format(i, j))
