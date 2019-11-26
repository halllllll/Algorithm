# 問題読んでやったことないと思って解こうとした（ログみたら以前に解いてたらしいが一切覚えてない）
# 自分より後ろにあるやつは優先度低い
n, x = map(int, input().split())
arr = list(map(int, input().split()))
c = 0
for i in range(1, n):
    if arr[i - 1] + arr[i] > x:
        dif = arr[i - 1] + arr[i] - x
        if arr[i] >= dif:
            # 自分だけ犠牲になればいい
            arr[i] -= dif
        else:
            # 自分だけじゃ足りないぶん
            new_dif = dif - arr[i]
            arr[i] = 0
            arr[i - 1] -= new_dif
        c += dif
print(c)
