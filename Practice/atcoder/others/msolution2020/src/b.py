# a < b < c
a, b, c = map(int, input().split())
k = int(input())
greenok = False
if a < b:
    greenok = True
for _ in range(k):
    if greenok:
        c *= 2
    else:
        b *= 2
    if a < b:
        greenok = True
if a < b < c:
    print("Yes")
else:
    print("No")