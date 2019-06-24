# ハッシュで数えてキーでソートして+-1を全探索
# と思ったけど登場してないやつでもいける 3 5 なら4が2個になるのでN個から全探索

n = int(input())
arr = list(map(int, input().split()))
lis = [0 for _ in range(10**5+1)]
hash = dict()
for a in arr:
    lis[a] += 1

ans = 1
for i in range(1, 10**5):
    ans = max(ans, lis[i-1]+lis[i]+lis[i+1])

print(ans)
