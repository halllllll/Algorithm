# lbとubの差っぽい
# と思ったけど単純に[n//2]-[n//2-1]か
n = int(input())
arr = list(sorted(list(map(int, input().split()))))
print(arr[n//2] - arr[n//2 - 1])
