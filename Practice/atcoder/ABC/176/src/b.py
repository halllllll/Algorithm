n = list(input())
x = 0
for i in range(len(n)):
    x += int(n[i])
if x % 9 == 0:
    print("Yes")
else:
    print("No")