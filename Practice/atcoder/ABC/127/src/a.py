a, b = map(int, input().split())
if 0 <= a <= 5:
    print(0)
elif 6 <= a < 13:
    print(int(b / 2))
else:
    print(b)
