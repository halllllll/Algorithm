# 登場回数の最も多い文字を省いた文字を2で割る（ceil）
# ... でやろうとしたがサンプル3でハネられて駄目

from collections import Counter
from math import ceil

s = input()
print(Counter(s))
most_appeared = max(Counter(s).values())
print(len(s))
t = ceil((len(s) - most_appeared) / 2)
print(t)
