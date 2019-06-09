# 座標圧縮的なやつ
n = int(input())
arr = list(map(int, input().split()))
arr_with_idx = [[i, v] for i, v in enumerate(arr)]
arr_with_idx.sort(key=lambda x: x[1], reverse=True)
for v in arr_with_idx:
    print(v[0]+1)
