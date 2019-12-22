# 少ないので実際にやる
# あまりはループするので、0かループした時点で終了
a, b, c = map(int, input().split())
aa = a
lis = []
while True:
    aa = aa + a
    d = aa % b
    if b == 0 or d in lis:
        print("NO")
        exit()
    lis.append(d)
    if d == c:
        print("YES")
        exit()

