# DとPが小さいので全探索でいいっすか？
# -> 駄目みたいっすね（サンプルケース4が通らない）
d, g = map(int, input().split())
points = {}
for i in range(d):
    p, c = map(int, input().split())
    points[i + 1] = [p, c]


def rec(cur_point, cur_count, tmp_mincount):
    if cur_count > tmp_mincount:
        return 10 ** 10
    if cur_point >= g:
        return cur_count
    ret = 10 ** 10
    for k in points.keys():
        if points[k][0] > 0:
            if points[k][0] == 1:
                # ボーナスポイント加算
                points[k][0] -= 1
                ret = min(
                    ret,
                    rec(
                        cur_point + k * 100 + points[k][1], cur_count + 1, tmp_mincount
                    ),
                )
                # もとにもどす
                points[k][0] += 1
            else:
                # ふつうにi*100を足す
                points[k][0] -= 1
                ret = min(ret, rec(cur_point + k * 100, cur_count + 1, tmp_mincount))
                # もとにもどす
                points[k][0] += 1
    tmp_mincount = min(tmp_mincount, ret)
    return ret


print(rec(0, 0, 10 ** 10))
