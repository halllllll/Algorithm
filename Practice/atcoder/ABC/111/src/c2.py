n = int(input())
evens, odds = {}, {}
for i, v in enumerate(list(map(int, input().split()))):
    if i % 2 == 0:
        if v in evens:
            evens[v] += 1
        else:
            evens[v] = 1
    else:
        if v in odds:
            odds[v] += 1
        else:
            odds[v] = 1
evens = sorted(evens.items(), key=lambda x: x[1], reverse=True)
odds = sorted(odds.items(), key=lambda x: x[1], reverse=True)
if len(evens) == 1 and len(odds) == 1:
    if evens[0][0] == odds[0][0]:
        print(n // 2)
    else:
        print(0)
else:
    # このへんぶっちゃけ勘でやった
    if evens[0][0] == odds[0][0]:
        if len(evens) == 1:
            print(n // 2 - odds[1][0])
        elif len(odds) == 1:
            print(n // 2 - evens[1][0])
        else:
            print(
                min(n // 2 - evens[0][1] + n // 2 - odds[1][1],
                    n // 2 - evens[1][1] + n // 2 - odds[0][1]))
    else:
        print(n // 2 - evens[0][1] + n // 2 - odds[0][1])
