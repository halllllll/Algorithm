# 最長で5文字なのでN*Kでいける

s = input().rstrip()  # python、無駄に改行コードを扱いがち
k = int(input())

arr = set()
for i in range(len(s)):
    for j in range(1, min(k, len(s)-i)+1):
        arr.add(s[i:i+j])

arr = sorted(list(arr))
print(arr[k-1])
