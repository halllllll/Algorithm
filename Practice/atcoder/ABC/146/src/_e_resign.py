# そういう感じのしゃくとり?

n, k = map(int, input().split())
arr = list(map(int, input().split()))

c = 0
r = 0
cur_sum = 0
cur_amount = 0

for l in range(n):
    while r < n and cur_amount + 1 < k:
        print("now l:r = {}:{} {}".format(l, r, arr[l : r + 1]))
        # 右に伸ばした時に生じること
        cur_sum += arr[r]
        cur_amount += 1
        if cur_sum % k == cur_amount:
            print("great {}".format(arr[l : r + 1]))
            c += 1
        r += 1
    if cur_sum % k == cur_amount:
        print("great {}".format(arr[l : r + 1]))
        c += 1
    # 左を伸ばした時に生じること
    if r == l:
        r += 1
    else:
        cur_sum -= arr[l]
        cur_amount -= 1

print(c)
