# きりみんちゃん配信からきました
# 4で割りきれる数と奇数をぶつける（4で割り切れず2で割り切れるやつはまあはい）
n = int(input())
arr = list(map(int, input().split()))
dividable4 = 0
dividable2 = 0
odds = 0
for a in arr:
  if a % 4 == 0:
    dividable4 += 1
  elif a % 2 == 1:
    odds += 1
  elif a % 2 == 0:
    dividable2 += 1
print("Yes" if odds <= dividable4 or (odds - dividable4 == 1 and dividable2 == 0)  else "No")