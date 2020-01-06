h, w = map(int, input().split())
table = []
for _ in range(h):
    line = input()
    if line.count(".") != w:
        table.append(line)
table = [list(x) for x in zip(*table)]
ans = []
for t in range(len(table)):
    if table[t].count(".") != len(table[t]):
        ans.append(table[t])
ans = [list(x) for x in zip(*ans)]
for a in ans:
    print("".join(a))

