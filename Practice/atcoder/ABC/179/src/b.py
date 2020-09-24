n = int(input())
zorocount = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        zorocount += 1
    else:
        zorocount = 0
    if zorocount == 3:
        print("Yes")
        exit()
print("No")
