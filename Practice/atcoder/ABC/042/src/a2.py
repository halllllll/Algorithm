# 吸い込んでソートして[5, 5, 7]になるものっていう昔書いたやつがクレバーだった（忘れてた）
# 今回はまっさきに浮かんだやつで....
ok = [[5, 5, 7], [5, 7, 5], [7, 5, 5]]
stdin = list(map(int, input().split()))
print("YES" if stdin in ok else "NO")
