# 罠なんだけど8<=Nなので繰り下がらなくてよい
n = int(input())
for i in range(n - 7, n + 1):
    print(i)
