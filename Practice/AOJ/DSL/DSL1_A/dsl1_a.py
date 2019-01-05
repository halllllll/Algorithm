import sys
sys.setrecursionlimit(10**8)

n, q = list(map(int, input().split()))
arr = list(range(n))
rank = [0 for _ in range(n)]


def root(t):
    # 経路圧縮
    if t != arr[t]:
        arr[t] = root(arr[t])
    return arr[t]


def unite(x, y):
    rootx = root(x)
    rooty = root(y)
    # ランク付
    if rank[rootx] < rank[rooty]:
        arr[rooty] = rootx
    elif rank[rooty] < rank[rootx]:
        arr[rootx] = rooty
    elif rootx != rooty:
        arr[rooty] = rootx
        rank[rootx] += 1


def find(x, y):
    return root(x) == root(y)


for _ in range(q):
    command, x, y = list(map(int, input().split()))
    if command == 0:
        unite(x, y)
    else:
        print(1 if find(x, y) else 0)
