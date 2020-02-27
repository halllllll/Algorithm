# ソートして左右からとっていくが、可能ならば同じ数字が連続しないようにする
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)
print(arr)
