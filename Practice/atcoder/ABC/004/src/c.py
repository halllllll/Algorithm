# 30回で一周するのでそれに丸める
n = int(input())
arr = [i + 1 for i in range(6)]
for i in range(0, n % 30):
    # print("{}と{}".format(i % 5, i % 5+1))
    arr[i % 5], arr[i % 5+1] = arr[i % 5+1], arr[i % 5]

print("".join(map(str, arr)))
