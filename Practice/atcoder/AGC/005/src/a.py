# SはストックのS 存在するぶんだけTと相殺できる
# 消した数じゃなくて残った数を数えるってのを読み飛ばしてて1WA
# 変数ミスで1WA

x = input()
stock = 0
count = 0
for a in x:
    if a == "S":
        stock += 1
    else:
        if stock > 0:
            count += 2
            stock -= 1
print(len(x)-count)
