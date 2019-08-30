# 奇数の隣は必ず4の倍数でなくてはならない あとはどうでもよさそう
# ただし 1 4 1 は大丈夫だが 1 4 1 2 はダメ
n = int(input())
arr = list(map(int, input().split()))
dividable_four = 0
odds = 0
for a in arr:
    if a % 4 == 0:
        dividable_four += 1
    elif a % 2 == 1:
        odds += 1
if dividable_four >= odds:
    print('Yes')
elif odds - dividable_four == 1 and odds + dividable_four == n:
    print('Yes')
else:
    print('No')
