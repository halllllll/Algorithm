n = int(input())
AC, WA, TLE, RE = 0, 0, 0, 0
for _ in range(n):
    s = input()
    if s == "AC":
        AC += 1
    elif s == "TLE":
        TLE += 1
    elif s == "WA":
        WA += 1
    elif s == "RE":
        RE += 1
print(f"AC x {AC}")
print(f"WA x {WA}")
print(f"TLE x {TLE}")
print(f"RE x {RE}")