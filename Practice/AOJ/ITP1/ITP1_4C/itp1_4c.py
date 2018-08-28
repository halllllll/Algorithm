while True:
    s = input()
    try:
        # まさかの1/2=1だったので
        print(int(eval(s)))
    except:
        break
