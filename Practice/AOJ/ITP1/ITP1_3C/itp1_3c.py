
def check(lis):
    if lis[0] > lis[1]:
        return lis[::-1]
    else:
        return lis


while True:
    l = list(map(int, input().split()))
    if sum(l) == 0:
        break
    print(*check(l))
