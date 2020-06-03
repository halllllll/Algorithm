s = input()
c = len(s)
if c % 2 == 1:
  print("No")
  exit()
c //= 2
hi = "hi" * c
if s != hi:
  print("No")
else:
  print("Yes")