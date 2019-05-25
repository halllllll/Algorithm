# これは本番後の解説を見てしまったやつ
# 入力を逆からたどるunion find（出力も逆）
# rankするのめんどくさいからsetで数える

# ってやるだけだと思ってたら得点数えるのがよくわからん。各木の根の高さが結局必要じゃない？

n, m = map(int, input().split())

parents = [i for i in range(n)]


def root(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = root(parents[x])
        return parents[x]


def unite(a, b):
    a, b = root(a), root(b)
    if a != b:
        parents[b] = a


gets = []
for _ in range(m):
    gets.append(list(map(int, input().split())))

gets = reversed(gets)
ans = []
for g in gets:
    print(n - len(set(ans)))
