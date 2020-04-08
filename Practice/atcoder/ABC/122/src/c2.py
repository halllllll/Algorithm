# 累積和
n, q = map(int, input().split())
s = input()
arr = [0] * (2 * 10**5 + 10)
idx = 1
while idx < len(s):
    if s[idx - 1] == "A" and s[idx] == "C":
        arr[idx] += 1
    idx += 1
for i in range(1, len(arr)):
    arr[i] += arr[i - 1]
for _ in range(q):
    l, r = map(int, input().split())
    print(arr[r - 1] - arr[l - 1])
