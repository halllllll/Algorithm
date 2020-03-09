# 気づき
# ①+-+-+-..か-+-+-+...のふたつを試して小さい方
# ②満たさなくなったら帳尻を合わせる（いまみてるやつだけでいい)
# ③1<=i<=nに対して和が0でない -> a1≠0（これは①とかぶる）
# 累積和をとってインデックスの偶奇で判断

n = int(input())
arr = list(map(int, input().split()))
p, m = 0, 0  # 累積和
pn, mn = 0, 0  # （操作した回数の）カウント
for i in range(n):
    if i % 2 == 0:
        # pは正にしたい
        if p + arr[i] > 0:
            p += arr[i]
        else:
            # 少ない操作で和を大きくしたいので1との差を取る
            d = p + arr[i]  # 差
            pn += abs(1 - d)
            p = 1
    else:
        # pは負にしたい
        if p + arr[i] < 0:
            p += arr[i]
        else:
            # 少ない操作で和を小さくしたいので-1との差をとる
            d = p + arr[i]
            pn += abs(-1 - d)
            p = -1
for i in range(n):
    if i % 2 == 0:
        # mは負にしたい
        if m + arr[i] < 0:
            m += arr[i]
        else:
            # ry
            d = m + arr[i]
            mn += abs(-1 - d)
            m = -1
    else:
        # mは正にしたい
        if m + arr[i] > 0:
            m += arr[i]
        else:
            # ry
            d = m + arr[i]
            mn += abs(1 - d)
            m = 1

print(min(pn, mn))
