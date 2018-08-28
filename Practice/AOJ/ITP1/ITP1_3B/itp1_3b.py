count = 1
while True:
    x = int(input())
    if x is not 0:
        print("Case {c}: {x}".format(c=count, x=x))
    else:
        break
    count += 1
