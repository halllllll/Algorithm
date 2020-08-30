n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = -10**10
group_id = 0
group_arr = [-1] * n
group_length = {}
# とりあえずグループ分けはできそう（せいぜいNなので）
for i in range(n):
    j = i
    friends = []
    while group_arr[j] == -1:
        friends.append(j)
        group_arr[j] = group_id
        j = p[j] - 1
    if len(friends) > 0:
        group_length[group_id] = friends
        group_id += 1

for gid, gsets in group_length.items():
    arr = gsets[:]
    scores = [0] * len(gsets)
    for i in range(min(len(gsets), k)):
        for j in range(len(gsets)):
            scores[j] += c[arr[j] - 1]
            ans = max(ans, scores[j])
            print(arr[j])
            # arr[j] = arr[arr[j]]
        print(scores)
print(ans)