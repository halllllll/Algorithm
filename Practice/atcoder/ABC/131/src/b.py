# 0からの差が小さいもの（絶対値が0に近いもの）を選ぶ
n, l = map(int, input().split())
arr = [i + l for i in range(n)]
s = sum(arr)
idx = -1
mindif = 10 ** 9
for i, a in enumerate(arr):
    if mindif > abs(a):
        mindif = abs(a)
        idx = i
print(s - arr[idx])
