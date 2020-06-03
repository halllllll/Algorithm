# R*r + G*g + B*b == N の数
# python3では間に合わないのでpypyで提出

R, G, B, N = map(int, input().split())
R, G, B = list(sorted([R, G, B], reverse=True))
ans = 0
for r in range(N + 1):
    for g in range(N + 1):
        if (N - (r * R + g * G)) % B != 0:
            continue
        b = (N - (r * R + g * G))/B
        if b < 0:
            break
        if r * R + g * G + b * B == N:
            ans += 1
        elif r * R + g * G + b * B > N:
            break

print(ans)
