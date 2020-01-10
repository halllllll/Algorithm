# まあ探索しましょうや 最低の2でも10回やりゃ1000越えるんだし
ans = 0
x = int(input())
if x == 1:
    print(1)
    exit()
for b in range(2, int(x * 0.5) + 1):
    p = 2
    while True:
        if b ** p > x:
            break
        ans = max(ans, b ** p)
        p += 1
print(ans)
