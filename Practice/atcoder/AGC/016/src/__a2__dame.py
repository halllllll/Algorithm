# 何度目のアタックだよ
# 全探索...（解答みた）
# え なにこれ 実装できんくない？

s = input()
lis = list(set(s))
ans = 0
for c in lis:
  t = s
  while len(set(t)) > 1:
