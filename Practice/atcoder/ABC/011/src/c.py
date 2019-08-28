# 0からスタートしてnまでたどるが挑戦回数は100回まで
# 大きい数から試してダメなら小さいやつにしていく

n = int(input())
ng = [int(input()) for _ in range(3)]
count = 0
ni = 0
flag = True
while True:
    if ni == n:
        break
    if count == 100:
        flag = False
        break
    if ni + 3 not in ng and ni + 3 <= n:
        ni += 3
    elif ni + 2 not in ng and ni + 2 <= n:
        ni += 2
    elif ni + 1 not in ng and ni + 1 <= n:
        ni += 1
    else:
        flag = False  # これ忘れてた
        break
    count += 1

if flag:
    print("YES")
else:
    print("NO")
