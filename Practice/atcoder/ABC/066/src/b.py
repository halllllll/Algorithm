s = input()
for i in range(len(s) - 2, 0, -1):
    target_s = s[:i]
    if len(target_s) % 2 != 0:
        continue
    if target_s[: int(len(target_s) / 2)] == target_s[int(len(target_s) / 2) :]:
        print(len(target_s))
        exit()
