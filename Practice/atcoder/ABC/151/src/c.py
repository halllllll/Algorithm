n, m = map(int, input().split())
table = {}
ac = 0
pena = 0
pena_arr = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = input().split()
    a = int(a)
    if a in table:
        continue
    if b == "AC":
        ac += 1
        table[a] = True
    elif b == "WA":
        pena_arr[a] += 1
pena = 0
for i in range(1, n + 1):
    if pena_arr[i] > 0 and i in table:
        pena += pena_arr[i]
print(ac, pena)
