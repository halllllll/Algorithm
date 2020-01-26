# 体力でかいやつに使ったほうがいいよね
n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))[::-1]
if k >= n:
    print(0)
    exit()
print(sum(arr[k:]))
