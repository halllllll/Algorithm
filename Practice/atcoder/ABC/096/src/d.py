# まず55555以下の素数っていくつあるん？->5637個あった
# 「どの異なる5個を選んでも」がむずい これがなければNの偶奇で2をとるかどうかがわかりそうだけど（？）
#  (30分ほど考えるがまったく無理 1byteすら書けない)
# （解説配信みる）（残り5分ほどでDを解説してるの草）
# （配信の解説を見てめちゃくちゃデカい声出た）（脱帽）（拍手）
n = int(input())
primes = []


def isprime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


for i in range(2, 55555 + 1):
    if isprime(i) and str(i)[-1] == "1":
        primes.append(i)

print(" ".join(list(map(str, (primes[:n])))))
