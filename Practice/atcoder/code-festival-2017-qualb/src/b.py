n = int(input())
d = {}
for v in list(map(int, input().split())):
    if v in d:
        d[v] += 1
    else:
        d[v] = 1

m = int(input())
for v in list(map(int, input().split())):
    if v in d and d[v] > 0:
        d[v] -= 1
    else:
        print("NO")
        exit()
print("YES")
