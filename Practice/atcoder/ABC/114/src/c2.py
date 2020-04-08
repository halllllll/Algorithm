# bitDPやりたくなるけどあきらかにオーバーキル
# ふつうにDFSする
n = int(input())


def dfs(cur):
    ret = 0
    for m in ["3", "5", "7"]:
        nex = cur
        nex += m
        if int(nex) <= n:
            if "7" in nex and "5" in nex and "3" in nex:
                ret += 1
            ret += dfs(nex)
    return ret


print(dfs(""))
