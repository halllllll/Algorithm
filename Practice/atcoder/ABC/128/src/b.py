# 辞書順かつ大きい順（リスト）
n = int(input())
hash = {}
for i in range(n):
    s, p = input().split()
    p = int(p)
    if s in hash.keys():
        hash[s].append([i, p])
    else:
        hash[s] = list()
        hash[s].append([i, p])

hash = sorted(hash.items())
for k, v in hash:
    vs = sorted(v, key=lambda x: x[1], reverse=True)
    for i in vs:
        print(i[0]+1)
