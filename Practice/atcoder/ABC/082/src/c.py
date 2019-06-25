# やればいい
# "取り除く"ことしかできないことを誤読していて（増やせると思ってた）3WA
n = int(input())
arr = list(map(int, input().split()))
d = dict()
for a in arr:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

count = 0
for k, v in d.items():
    if k != v:
        if k < v:
            count += v-k
        else:
            count += v
print(count)
