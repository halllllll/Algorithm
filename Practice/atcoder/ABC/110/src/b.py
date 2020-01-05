# max min
n, m, x, y = map(int, input().split())
xs = max(list(map(int, input().split())))
ys = min(list(map(int, input().split())))

print("No War" if xs < ys and x <= xs and ys <= y else "War")
