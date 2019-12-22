a, b = input(), input()
for i in range(1, 4):
    i = str(i)
    if i not in [a, b]:
        print(i)
        exit()

