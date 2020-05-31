n = int(input())
ans = 1
arr = sorted(list(map(int, input().split())))
for a in arr:
    if ans * a > 10**18:
        print(-1)
        exit()
    else:
        ans *= a
print(ans)