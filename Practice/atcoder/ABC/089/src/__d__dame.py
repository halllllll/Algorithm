# h*wの1次元配列で各要素に(i,j)のインデックスでもぶちこんどけばやるだけに見えるが
# なぜかTLEなる あとREがあるのはまあ雑にやったからいいとしてなんかしらんけどWAが一つある....

h, w, d = map(int, input().split())
arr = [() for _ in range((h + 1) * (w + 1))]
table = []
for y in range(h):
    line = list(map(int, input().split()))
    arr.append(line)
    for x in range(w):
        arr[line[x]] = (y + 1, x + 1)

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(ds[r] - ds[l])
    # ans = 0
    # for x in range(l, r, d):
    #     ans += abs(arr[x][1] - arr[x + d][1]) + abs(arr[y][0] - arr[y + d][0])
    # print(ans)
