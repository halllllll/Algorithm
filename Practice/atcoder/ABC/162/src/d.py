# (R, B)の間にあるGみたいな感じ 6種類あるのか？ 6*N^2
n = int(input())
s = input()
rs, gs, bs = [0] * n, [0] * n, [0] * n
if s[0] == "R":
    rs[0] = 1
elif s[0] == "G":
    gs[0] = 1
elif s[0] == "B":
    bs[0] = 1
for i in range(1, n):
    rs[i] = 1 + rs[i - 1] if s[i] == "R" else rs[i - 1]
    gs[i] = 1 + gs[i - 1] if s[i] == "G" else gs[i - 1]
    bs[i] = 1 + bs[i - 1] if s[i] == "B" else bs[i - 1]
ans = 0
for i in range(0, n):
    for j in range(i + 2, n):
        if (s[i] == "R" and s[j] == "B") or (s[i] == "B" and s[j] == "R"):
            ans += gs[j]
            ans -= gs[i]
            if (i + j) % 2 == 0 and s[(i + j) // 2] == "G":
                ans -= 1
        elif (s[i] == "R" and s[j] == "G") or (s[i] == "G" and s[j] == "R"):
            ans += bs[j]
            ans -= bs[i]
            if (i + j) % 2 == 0 and s[(i + j) // 2] == "B":
                ans -= 1
        elif (s[i] == "B" and s[j] == "G") or (s[i] == "G" and s[j] == "B"):
            ans += rs[j]
            ans -= rs[i]
            if (i + j) % 2 == 0 and s[(i + j) // 2] == "R":
                ans -= 1
print(ans)
