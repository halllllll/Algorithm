n = int(input())
for i in range(1, 50000):
    if n == int(i * 1.08):
        print(i)
        exit()
print(":(")

