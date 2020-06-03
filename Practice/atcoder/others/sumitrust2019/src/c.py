x = int(input())
start = 100
end = 100000
flag = False
for i in range(1, int(end / start) + 1):
    if start <= x <= start + i * 5:
        flag = True
        break
    else:
        start += 100

print("1" if flag else "0")
