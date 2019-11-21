# N, M<=10なので全探索の気持ちが生える
# -> N個のスイッチについて0,1のすべての状態を想定し、
#   それぞれについてみたとき、各電球が条件を満たしているか都度判断する

n, m = map(int, input().split())
balbs = [[] for _ in range(m)]
for i in range(m):
    # zero order
    connectswtiches = list(map(lambda x: int(x) - 1, input().split()))[1:]
    balbs[i] = connectswtiches

correct_state = list(map(int, input().split()))

# 2^N
def f(cur, n):
    if n == 0:
        # 判定
        for i, balb in enumerate(balbs):
            on_switch_count = 0
            for swtich_n in balb:
                if cur[swtich_n] == 1:
                    on_switch_count += 1
            if correct_state[i] != on_switch_count % 2:
                return 0
        return 1

    ret = 0
    lnh = len(cur)
    nex = cur[:]
    nex[lnh - n - 1] = 1
    ret += f(nex, n - 1)
    nex[lnh - n - 1] = 0
    ret += f(nex, n - 1)
    return ret


print(f([0 for _ in range(n)], n))
