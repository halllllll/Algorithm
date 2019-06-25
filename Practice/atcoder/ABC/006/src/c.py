# a+b+c = N, 2*a + 3*b + 4*c = M
# だけかと思ったけどTLEになるのはいいとしてWAになるのは完全に意味不明なんだが
#
n, m = map(int, input().split())

for a in range(n + 1):
    for b in range(n - a + 1):
        c = n - a - b
        if c < 0 or 2 * a + 3 * b + 4 * c > m:
            break
        if 2 * a + 3 * b + 4 * c == m:
            print(a, b, c)
            exit()

print(-1, -1, -1)
