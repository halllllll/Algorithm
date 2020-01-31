# ソートしたやつの小さい方から2つを決めてもうひとつはにぶたん
# 3, 5としたときに残りの一つは5, 6, 7みたいになる
# このにぶたんなんか実装がめっっっちゃむずくない？サンプル1が通らんのだが
# やったけどTLEなるな
# 手元で限界値までのサンプルを作って動かしたら3秒ちょい？とかなのでたぶんPypyなら通る


n = int(input())
arr = sorted(list(map(int, input().split())))


def lower_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l


ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        idx_l = lower_bound(arr, arr[i] + arr[j]) - 1
        ans += len(arr[j + 1 : idx_l + 1])
print(ans)
