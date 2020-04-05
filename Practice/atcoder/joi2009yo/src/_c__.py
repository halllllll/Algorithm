# これは難しくないですか？ぼくにとっては難しいです
# 全探索は愚っぽい気がするが思いつかないのでそうする
n = int(input())
arr = [int(input()) for _ in range(n)]


def dfs(a):
    # 消えるのは一回につきせいぜい一箇所
    # -> 4つ以上並んでる場所がみつかった時点でその部分を省いて終了
    flag = False
    idx = -1
    r = 0
    lnh = len(a)
    for l in range(lnh):
        if flag:
            break
        while r < lnh and a[l] == a[r]:
            r += 1
        if r - l >= 4:
            # この場所を省く
            flag = True
            idx = l
            break
        if r == l:
            r += 1
    if flag and idx >= 0:
        new_arr = a[:idx] + a[r:]
        return dfs(new_arr)
    else:
        # print("終了: {}".format(a))
        return lnh


ans = n
tmp1, tmp2, tmp3 = arr[:], arr[:], arr[:]
for i in range(n):
    tmp1[i], tmp2[i], tmp3[i] = 1, 2, 3
    ans = min(ans, dfs(tmp1), dfs(tmp2), dfs(tmp3))
    tmp1[i], tmp2[i], tmp3[i] = arr[i], arr[i], arr[i]
print(ans)