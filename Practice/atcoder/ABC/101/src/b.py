# Nは最大9桁
n = input()
sn = 0
for ni in n:
    sn += int(ni)
if int(n) % sn == 0:
    print("Yes")
else:
    print("No")
