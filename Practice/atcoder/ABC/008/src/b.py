n = int(input())
d = {}
for _ in range(n):
    x = input()
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

reverse_d = {}
for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
    print(k)
    exit()

