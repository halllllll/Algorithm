# きりみんちゃんのtwから来ました
# サンプルを眺めて、mがなんなのかはわからんけどとりあえずai(0<=i<n)ごとの ai mod mの最大値はai-1ということが生える（生えたよ）
# なので、mがなんなのかはわからんけど、とりあえずaiそれぞれの最大値を足した
n = int(input())
print(sum(list(map(lambda x: int(x) - 1, input().split()))))

