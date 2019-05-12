n, x, y = map(int, input().split())
arr = list(sorted(list(map(int, input().split())), reverse=True))
for i in range(n):
    if i % 2 == 0:
        # takahashi turn
        x += arr[i]
    else:
        y += arr[i]

if x > y:
    print("Takahashi")
elif y > x:
    print("Aoki")
else:
    print("Draw")
