n = int(input())
if n % 2 == 1:
    print("No")
    exit()
s = input()
print("Yes" if s[: n // 2] == s[n // 2 :] else "No")

