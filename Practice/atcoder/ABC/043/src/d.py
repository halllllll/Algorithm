# 二文字以上連続する箇所があったら確定 eialfisxxnidkaofkufdだとxxnとかを示せばいい
# 連続して無くても、（取りぬく部分文字列）全体の長さの過半数だとおｋ xnxはおｋ xlbxはダメ

# いまみている文字と同じ文字が次に出てくる最も近い場所を探索してその距離を求める？1or2なら確定
s = input()
a, b = -1, -1
for i in range(len(s) - 1):
    if i == len(s) - 2:
        # 次の一手しかみれない
        if s[i] == s[i + 1]:
            a, b = i + 1, i + 2
            break
    else:
        if s[i] == s[i + 1]:
            a, b = i + 1, i + 2
            break
        elif s[i] == s[i + 2]:
            a, b = i + 1, i + 3
            break

print(a, b)
