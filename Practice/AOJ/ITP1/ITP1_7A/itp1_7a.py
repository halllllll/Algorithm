while True:
    m, f, r = map(int, input().split())
    score = ""
    if all([x < 0 for x in [m, f, r]]):
        break
    if any([x < 0 for x in [m, f]]):
        score = "F"
    elif 80 <= m+f:
        score = "A"
    elif 65 <= m+f:
        score = "B"
    elif 50 <= m+f or (30 <= m+f and 50 <= r):
        score = "C"
    elif 30 <= m+f:
        score = "D"
    else:
        score = "F"
    print(score)
