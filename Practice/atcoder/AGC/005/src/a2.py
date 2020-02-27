# 最初にでてきたSでフラグ 備蓄がなくなるまでTとペアにしてなくなったらフラグしなおし
ST = input()
flag = False
pool_s = 0
pair = 0
flag = 0
for v in ST:
    if flag == False and v == "S":
        flag = True
        pool_s = 1
    elif flag and v == "T":
        if pool_s > 0:
            pair += 1
            pool_s -= 1
        else:
            pool_s = 0
            flag = False
    elif flag and v == "S":
        pool_s += 1
print(len(ST) - pair * 2)
