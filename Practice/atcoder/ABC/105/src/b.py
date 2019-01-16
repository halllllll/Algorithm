# N は 1 以上 100 以下の整数
n = int(input())
flag = False
for a in range(int(100/4)+1):
    if flag:
        break

    for b in range(int(100/7)+1):
        # print("4*{}+7*{} = {}".format(a, b, 4*a+7*b))
        if 4*a+7*b == n:
            flag = True
            break
        if 4*a+7*b > n:
            next

print('Yes' if flag else 'No')
