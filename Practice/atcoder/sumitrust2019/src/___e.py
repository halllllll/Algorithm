# なぜか途中からREなる...
# ので、Python3は捨ててPHPで解いた

n = int(input())
s = list(map(int, input().split()))
color = 0  # appeared_zero (0~2)
ans = 1
MOD = 1000000007
cur = [-1, -1, -1]
for c in s:
    if c == 0:
        cur[color] = 0
        color += 1
        ans %= MOD
    else:
        x = cur.count(c - 1)
        ans *= x
        ans %= MOD
        if c - 1 in cur:
            idx = cur.index(c - 1)
            cur[idx] += 1
        else:
            print("????????????")
            exit()
ans *= 3 if color == 0 else 3 if color == 1 else 6
ans %= MOD
print(ans)
