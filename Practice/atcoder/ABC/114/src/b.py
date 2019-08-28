x = list(input())
m = 9999999999
for i in range(len(x)-2):
    # 3つとる
    xxx = int(''.join(x[i:i+3]))
    m = min(m, abs(xxx-753))
print(m)
