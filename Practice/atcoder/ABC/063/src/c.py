# できるだけ点数が多いほうが嬉しいので、10の倍数にならないように低い点数を引いていく
n = int(input())
arr = list(sorted([int(input()) for _ in range(n)]))
s = sum(arr)
if s % 10 != 0:
    print(s)
else:
    for a in arr:
        if a % 10 == 0:
            continue
        else:
            print(s - a)
            exit()
    print(0)
