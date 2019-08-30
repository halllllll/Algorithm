billdings = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]


def printstate(billdings):
    for i in range(len(billdings)):
        for j in range(len(billdings[0])):
            for k in range(len(billdings[0][0])):
                print(" "+str(billdings[i][j][k]), end="")
            print()
        if i != len(billdings)-1:
            print("#"*20)


n = int(input())
for _ in range(n):
    b, f, r, v = map(int, input().split())
    b, f, r = b-1, f-1, r-1
    billdings[b][f][r] += v

printstate(billdings)
