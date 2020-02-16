n = int(input())
arr = filter(lambda x: x % 2 == 0, list(map(int, input().split())))
for a in arr:
  if a % 3 == 0 or a % 5 == 0:
    continue
  else:
    print("DENIED")
    exit()
print("APPROVED")