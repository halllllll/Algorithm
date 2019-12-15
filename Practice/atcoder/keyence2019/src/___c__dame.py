# Ai>=Bi 出来るならそのままにする
# Ai < Bi 仕方ないので溢れたぶんを使う
# 「変更したAi」の最小値が欲しいので、使うのは余ってるやつが多い順に使ったほうがいい

n = int(input())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

lack, lack_i = 0, []
extra, extra_i = 0, []
for i in range(n):
    if arr[i] < brr[i]:
        lack += brr[i] - arr[i]
        lack_i.append([i, brr[i] - arr[i], False])
    else:
        extra += arr[i] - brr[i]
        extra_i.append([i, arr[i] - brr[i], False])

if lack > extra:
    print(-1)
    exit()

# 大量に余っているやつから優先的に使う
extra_i = list(sorted(extra_i, key=lambda x: x[1], reverse=True))
ans = 0

l_i = 0
e_i = 0

while True:
    if l_i >= len(lack_i):
        break
    while True:
        if e_i >= len(extra_i):
            print(-1)
            exit()
        if lack_i[l_i][1] <= extra_i[e_i][1]:
            extra_i[e_i][2] = True  # 一回でも使用した
            ans += 1  # 少ないやつを潰したぶん
            extra_i[e_i][1] -= lack_i[l_i][1]
            break
        else:
            extra_i[e_i][2] = True  # 一回でも使用した
            e_i += 1
            lack_i[l_i][1] -= extra_i[e_i][1]
            extra_i[e_i][1] = 0
    l_i += 1

bonus = len(list(filter(lambda x: x[2] == True, extra_i)))
print(ans + bonus)
