# Cは整数のC
# a + b + c = yなのでそういうことです
# オーダーの見積もり典型問題

n, y = map(int, input().split())

for a in range(2000+1):
    for b in range(2000+1):
        c = n - a - b
        if c < 0:
            break
        if a * 10000 + b * 5000 + c * 1000 == y:
            print("{} {} {}".format(a, b, c))
            exit()

print(-1, -1, -1)
