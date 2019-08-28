# じゃあ全部保存していってやるよ
# atcoderのpython3のバージョンが古すぎて(3.4.3)TypeError: unhashable type: 'list'なるのでため息つきながら直した

n = int(input())
d = {}
arr = []
for _ in range(n):
    x = "".join(list(map(str, list(sorted(input())))))
    arr.append(x)
    if x not in d:
        d[x] = 1
    else:
        d[x] += 1

c = 0
for a in arr[:0:-1]:
    if d[a] > 0:
        c += d[a] - 1
        d[a] -= 1

print(c)
