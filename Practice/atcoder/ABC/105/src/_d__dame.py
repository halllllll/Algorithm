# 累積和でいけるんですか？

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ruiseki_arr = [0] * n
ruiseki_arr[0] = arr[0]
for i in range(1, n):
    ruiseki_arr[i] = ruiseki_arr[i - 1] + arr[i]
ans = 0
ans_arr = []
for i in range(n):
    for j in range(i, n):
        if i > 0:
            target = ruiseki_arr[j] - ruiseki_arr[i - 1]
        elif i == j:
            target = arr[i]
        else:
            target = ruiseki_arr[j]
        if target % m == 0:
            ans += 1
print(ans)