# 小さい順にa, b, cとしてaを決め打ち、bとcでダブル尺取
# (小さい順に並ぶのでa<b+cとb<a+cは確定 残るc<a+bを調べる)

n = int(input())
print("n = ", n)
arr = sorted(list(map(int, input().split())))
print(arr)

a, b, c = 0, 1, 2
count = []
