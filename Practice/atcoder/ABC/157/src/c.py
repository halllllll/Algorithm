n, m = map(int, input().split())
if n == 1 and m == 0:
    print(0)
    exit()
ans = ["-" for _ in range(n)]

for _ in range(m):
    s, c = map(int, input().split())
    if n == m == 1 and s == 1 and c == 0:
        print(0)
        exit()
    if s == 1 and c == 0:
        print(-1)
        exit()
    if ans[s - 1] == "-":
        ans[s - 1] = c
    else:
        if ans[s - 1] != c:
            print(-1)
            exit()

for i, a in enumerate(ans):
    if i == 0:
        if a == "-":
            print(1, end="")
        else:
            print(a, end="")
    else:
        if a == "-":
            print(0, end="")
        else:
            print(a, end="")

