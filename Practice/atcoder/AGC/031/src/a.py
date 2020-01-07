# 最終的な倒叙回数だけで決まりそうな気がした(登場回数+1を掛けて最後に空文字ぶん1を引く)
# なんでかというと、同じ文字は含まないので、結局登場する順番は関係ないから。ある文字が複数あったとき、ひとつだけ選ぶ（あるいは選ばない）というのは、「どの時点で登場した文字を採用するか」と同義。
# などとドヤったけど6WAくらいだしましたしにます
# と思ったらMODしてなかった件


from functools import reduce

n = int(input())
s = input()
d = {}
for sv in s:
    if sv not in d:
        d[sv] = 1
    else:
        d[sv] += 1
ans = reduce(lambda x, y: x * y, list(map(lambda x: x[1] + 1, d.items()))) - 1
print(ans % (10 ** 9 + 7))
