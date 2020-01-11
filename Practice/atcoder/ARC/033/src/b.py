# 集合演算するだけ おしまい
n, m = map(int, input().split())
arr = set(list(map(int, input().split())))
brr = set(list(map(int, input().split())))
print(len(arr & brr) / len(arr | brr))
