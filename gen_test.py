from random import randint

t = 10 ** 3
N = 2 * t

with open("testcase.txt", mode="w") as f:
    f.write(str(N) + "\n")
    line = " "
    for _ in range(N):
        i = randint(1, t)
        line += str(i) + " "
    f.write(line)

