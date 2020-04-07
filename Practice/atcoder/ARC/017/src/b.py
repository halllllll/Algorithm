# 尺取でやる
# めっっっっっちゃくちゃ実装しにくい
# 典型しかできないからだね 圧倒的に精進と能力が足りてないね
# 後半の帳尻合わせがマジでわけわからん
# コーナーケース卑怯

n, k = map(int, input().split())
if k == 1:
    print(n)
    exit()
arr = [int(input()) for _ in range(n)]
l, r = 0, 0
ans = 0
while l <= n - k:
    while r < n - 1 and arr[r] < arr[r + 1]:
        r += 1
        if r - l == k - 1:
            # 規定の長さに達したため終了
            ans += 1
            break
    if r - l != k - 1:
        # 途中で単純増加にならなくなった場合、いまみてるl~l+kでは挽回不可能なので、そこまですすめる
        l = r + 1
    else:
        # 長さぴったりの場合、次のループのため帳尻合わせ
        l += 1
    if l >= r:
        # 帳尻合わせ
        r = l
    # print("次のスタート時 l, r = {}, {}".format(l, r))
print(ans)