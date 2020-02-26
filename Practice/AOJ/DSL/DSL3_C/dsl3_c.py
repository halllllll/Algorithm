# しゃくとりはO(N)なので数え上げられそう

n, q = map(int, input().split())
arr = list(map(int, input().split()))

for x in list(map(int, input().split())):
    ans = 0
    r = 0
    tmp = 0
    for l in range(n):
        while r < n and tmp <= x:
            tmp += arr[r]
            r += 1
            ans += 1
            if tmp == x:
                break
        print("l:r = {}:{} -> {} temp : {}".format(l, r, arr[l:r], tmp))
        if r == l:
            r += 1
        else:
            tmp -= arr[l]
    print(ans)
