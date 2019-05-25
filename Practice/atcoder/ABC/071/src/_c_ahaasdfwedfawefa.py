# カウントしていっていけるやつで比較
# 2つ以上の最大のやつと2番目に大きいやつ vs 4つ以上の最大のやつ


# は？REとか謎いんだけど

n = int(input())
arr = [0 for _ in range(10**5)]
for i in list(map(int, input().split())):
    arr[i - 1] += 1

ans = 0
overtwo = []
overfour = []
for idx, a in enumerate(arr):
    if a >= 4:
        overfour.append(idx + 1)
    elif a >= 2:
        overtwo.append(idx + 1)

if overfour != [] or len(overtwo) > 1:
    if len(overfour) != 0 and len(overtwo) > 1:
        ans = max(overfour[-1] * 4, overtwo[-1] * overtwo[-2])
    elif len(overfour) != 0:
        ans = overfour[-1] * 4
    else:
        ans = overtwo[-1] * overtwo[-2]
print(ans)
