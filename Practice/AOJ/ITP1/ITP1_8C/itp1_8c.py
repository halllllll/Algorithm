from string import ascii_lowercase
import sys  # 何行くるかわからんのクソ問題
table = dict(zip(ascii_lowercase, [0 for _ in range(len(ascii_lowercase))]))

for s in sys.stdin:
    for c in s:
        if c.lower() in table:
            table[c.lower()] += 1
for k, v in table.items():
    print("{} : {}".format(k, v))
