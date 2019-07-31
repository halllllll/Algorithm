# 最大値と二番目に大きいやつをとっておく。最大値のときだけ二番目に大きいやつ採用
n = int(input())
arr = []
for i in range(n):
  t = int(input()) 
  arr.append([i, t])

sorted_arr = list(sorted(arr, key = lambda x : x[1]))
biggest = sorted_arr[-1]
second_biggest = sorted_arr[-2]

for i in range(n):
  if i != biggest[0]:
    print(biggest[1])
  else:
    print(second_biggest[1])
