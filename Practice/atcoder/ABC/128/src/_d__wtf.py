# 捨てるのは最後でいいのはわかったけど実装が浮かばず、結局DPとか必要なんじゃないの？と思った
# ら、単純に左からa個右からb個取ったら捨てる操作はk-(a+b)だから〜、というらしい
# なぜか2つWAが取れない
# ??????????????????

n, k = map(int, input().split())
v = list(map(int, input().split()))
ans = -(10 ** 9)
for a in range(n):
    for b in range(n):
        if a + b <= min(n, k):
            arr = sorted(v[:a] + v[n - b :])
            tmp = 0
            for ai in range(k - (a + b)):
                if ai >= len(arr):
                    break
                if arr[ai] < 0:
                    tmp += arr[ai]
                else:
                    break
            # print("a, b = {}, {}".format(a, b))
            # print("now arr: {}".format(arr))
            ans = max(ans, sum(arr) - tmp)
            # print("now ans = {}".format(ans))
        else:
            break
print(ans if ans != -(10 ** 9) else 0)
