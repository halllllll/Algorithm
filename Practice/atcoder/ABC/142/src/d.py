# なんとなく薄目でみていると素因数分解したやつの底の共通するうちから2つ選ぶのが浮かんでくる
# と思ったけど共通するやつの数でいいのか？サンプルケース2おかしないか
# 素因数分解の方法が間違っていた

a, b = map(int, input().split())


def ff(x):
    if x == 1 or x == 2:
        return True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def f(x):
    ret = []
    i = 1
    while i * i <= x:
        if x % i == 0:
            if ff(i):
                ret.append(i)
            # 最初と最後が重複しないか確認
            if i != 1 and i * i != x:
                if ff(x // i):
                    ret.append(x // i)
        i += 1
    if ff(x):
        ret.append(x)
    return set(ret)


a_lis, b_lis = f(a), f(b)
common_lis = a_lis & b_lis
print(len(common_lis))
