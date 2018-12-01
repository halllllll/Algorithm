arr = [int(n) if n.isnumeric() else n for n in list(map(str, input().split()))]
stack = []
for v in arr:
    if(type(v) is int):
        stack.append(v)
    else:
        # 取り出す順に注意
        b, a = stack.pop(), stack.pop()
        nx = a+b if v == "+" else a-b if v == "-" else a*b
        stack.append(nx)
print(stack.pop())
