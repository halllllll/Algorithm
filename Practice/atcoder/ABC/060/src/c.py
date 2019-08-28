# トリガーされたらステップ踏んで[i]>[i-1]+Tまでいったときに加算できるのはスタートしてから終わるまでにTを加えたぶんだけ
# ん？？？サンプル3の出力おかしない？


n, t = map(int, input().split())
arr = list(map(int, input().split()))
# ans = t  # どうせ最後一回なるので
ans = 0  # テスト
tmp = arr[0]
pre = arr[0]
for i in range(1, n):
    print(tmp, arr[i], ans)
    if tmp + t <= arr[i]:
        print("リセット", tmp - pre + t)
        # リセットされる場合のみ加算
        ans += tmp - pre + t
        pre = arr[i]
    else:
        ans += arr[i]-tmp

    tmp = arr[i]


print(ans)
