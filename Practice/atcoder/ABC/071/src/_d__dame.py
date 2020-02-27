# 直前が縦にそろっているかどうかで決まりそうだけどわからない

n = int(input())
s = [list(input()), list(input())]
MOD = 10 ** 9 + 7
ans = 1
vertical = False
i = 0
if n == 1:
    print(3)
    exit()
while i < n:
    if i == 0:
        if s[0][i] == s[1][i]:
            ans = 3
            i += 1
            vertical = True
        else:
            ans = 6
            i += 2
            vertical = False
    else:
        if s[0][i] == s[1][i]:
            if vertical:
                ans = (ans * 2) % MOD
            else:
                # 直前のiにより色は一意に決まっている
                vertical = True
            i += 1
        else:
            if vertical:
                ans = (ans * 3) % MOD
                vertical = False
            else:
                # 直前のiにより色は一意に決まっている
                vertical = False
            i += 2

print(ans)

