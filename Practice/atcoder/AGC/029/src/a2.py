# Bはすべて右に詰まるので各Bの右からの距離の総和
# （逆でもいい Wの左）
s = input()
n = len(s)
w = 0
pack_w = 0
for i in range(n):
    if s[i] == "W":
        w += i - pack_w
        pack_w += 1

print(w)
