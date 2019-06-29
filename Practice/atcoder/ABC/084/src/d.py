# 毎回やってもたかがしれてそう -> 間に合いませんでした
# 素直に累積和+包除原理を使う

arr = [0 for _ in range(10 ** 5 + 1)]


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


for i in range(3, 10**5+1):
    if isPrime(i) and isPrime(int((i + 1) / 2)):
        arr[i] = 1
    arr[i] += arr[i-1]

q = int(input())


for _ in range(q):
    l, r = map(int, input().split())
    print(arr[r] - arr[l-1])
