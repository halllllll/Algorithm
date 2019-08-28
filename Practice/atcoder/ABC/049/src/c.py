# デジャヴュ。ゼロから始めるのではなく消していってゼロにする
# なぜか1WA
# ほとんど同じはずのこのコードだと通った 意味不明

s = input()
while True:
    if len(s) == 0:
        print("YES")
        exit()
    elif len(s) <= 4:
        print("NO")
        exit()
    else:
        # 長さの処理しなくてもエラーにはならんっぽい
        if s[-7:] == "dreamer":
            s = s[:-7]
        elif s[-6:] == "eraser":
            s = s[:-6]
        elif s[-5:] == "dream" or s[-5:] == "erase":
            s = s[:-5]
        else:
            print("NO")
            break
