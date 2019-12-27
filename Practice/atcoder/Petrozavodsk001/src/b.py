# 2行として上にa下にbを並べた時にai<biなら確実に同じ数にできる(同じインデックス同士だと1ずつ狭まるので)
# ai>biのときはai-bi回加算しなくてはならない 加算できる数はai<biの全てのiの(bi-ai)/2回分
n = int(input())
a, b = list(map(int, input().split())), list(map(int, input().split()))

pool = 0
use = 0
for i in range(n):
    if a[i] < b[i]:
        pool += (b[i] - a[i]) // 2
    elif b[i] < a[i]:
        use += a[i] - b[i]

print("Yes" if pool >= use else "No")
