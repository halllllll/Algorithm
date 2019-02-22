# 再帰で3,5,7を振り分けるのめんどくさそうだなと思ったら、
# 振り分けずに0個以上あればあればいいセットを作ってそこから省く、という手段を使うのか...

n = int(input())
sitigosan = []


def f(i):
    if i <= 10 ** 9:
        sitigosan.append(i)
        f(i * 10 + 3)
        f(i * 10 + 5)
        f(i * 10 + 7)


f(3)
f(5)
f(7)
# これだと3から埋めていってダメだと5、7に変えていってるので昇順に並んでない
sitigosan = sorted(sitigosan)
count = 0
for sgs in sitigosan:
    if sgs > n:
        break
    str_sgs = str(sgs)
    if "3" in str_sgs and "5" in str_sgs and "7" in str_sgs:
        count += 1
print(count)
