# 0~kまでx個左から取り、0~k-xまで右からy個取り、最後に0~k-x-yまで取ったうちで小さいやつを捨てる
n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for x in range(k + 1):
    for y in range(k - x + 1):
        for z in range(k - x - y + 1):
            if x + y < z or x + y + z > k:
                continue
            arr_tmpx = []
            arr_tmpy = []
            if x > 0:
                arr_tmpx = arr[:x]
            if y > 0:
                arr_tmpy = arr[-y:]
            arr_tmpx.extend(arr_tmpy)
            arr_tmpx = sorted(arr_tmpx)
            m = 0
            sorted_arr_tmpx = sorted(arr_tmpx)
            for zi in range(z):
                if sorted_arr_tmpx[zi] >= 0:
                    break
                m += sorted_arr_tmpx[zi]
            print(sorted_arr_tmpx, x, y, z, "m=:", m)

            ans = max(ans, sum(arr_tmpx)-m)

print(ans)
