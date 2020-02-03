# まったくわからんので実験する
# 実験の結果、素数同士だと回数が大きくなる 差は近くなくても大きくなる
# 最後がa,b=0,1、その前は1,2, その前は2,3, その前は3,5, その前は5,8, その前は8,13...というふうに、a,bとすると次はb,a+bみたいになる？


k = int(input())
a, b = 0, 1
c = 0
while c < k:
    c += 1
    a, b = b, a + b
# print("answer: ")
print(a, b)

# def gcd(a, b, count):
#     if a > b:
#         return gcd(b, a, count)
#     print(a, b, count)
#     if a == 0:
#         print("count = {} で終了".format(count))
#         return b
#     else:
#         return gcd(b%a, a, count + 1)

# print(gcd(314159265, 358979323, 1))
# print(gcd(144, 233, 1))
