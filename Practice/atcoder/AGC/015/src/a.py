# 3 .. 6 N=4とすると真ん中2つは(3, 3)~(6, 6)までで、1ずつインクリメントして全種類網羅できる
# 3+3 ~ 6+6までの12-6+1種類
n, a, b = map(int, input().split())
if a == b and n == 1:
    print(1)
elif b < a or n == 1:
    print(0)
elif n == 2 and a <= b:
    print(1)
else:
    minn = (n - 2) * a
    maxn = (n - 2) * b
    print(maxn - minn + 1)
