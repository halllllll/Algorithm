# a1が決まればb1,b2,b3が決まり、b1が決まればa,a3が決まる
table = [list(map(int, input().split())) for _ in range(3)]
for a1 in range(101):
    b1 = table[0][0] - a1
    b2 = table[1][0] - a1
    b3 = table[2][0] - a1
    a2 = table[0][1] - b1
    a3 = table[0][2] - b1
    if (
        a2 + b2 == table[1][1]
        and a3 + b2 == table[1][2]
        and a2 + b3 == table[2][1]
        and a3 + b3 == table[2][2]
    ):
        print("Yes")
        exit()
print("No")
