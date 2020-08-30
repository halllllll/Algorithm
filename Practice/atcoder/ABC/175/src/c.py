x, k, d = map(int, input().split())
if x >= 0:
    if x - k * d >= 0:
        print(x - k * d)
    else:
        # 最初に負になってしまうところとその直前を巡回する
        ok, ng = k, 0
        while (ok - ng) > 1:
            mid = (ok + ng) // 2
            if x - mid * d <= 0:
                # いきすぎ
                ok = mid
            else:
                ng = mid
        # ok回目で負にたどり着く？
        rest = k - ok
        if rest % 2 == 0:
            # いまいるところに戻ってこれる
            print(abs(x - ok * d))
        else:
            # 一回正方向にいどうしたもの
            print(x - (ok - 1) * d)
else:
    if x + k * d <= 0:
        print(abs(x + k * d))
    else:
        # 最初に正になるところ
        ok, ng = k, 0
        while (ok - ng) > 1:
            mid = (ng + ok) // 2
            if x + mid * d >= 0:
                ok = mid
            else:
                ng = mid
        rest = k - ok
        if rest % 2 == 0:
            print(x + ok * d)
        else:
            print(abs(x + ok * d - d))