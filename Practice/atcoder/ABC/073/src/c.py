# mapして偶数なら0奇数なら1
n = int(input())
dic = {}
for _ in range(n):
    x = int(input())
    if x in dic:
        del dic[x]
    else:
        dic[x] = 1

print(len(dic))
