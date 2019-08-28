'''
エラトステネスの篩をやるよ
'''

def eratosthenes(n):
    if n<1:
        return -1
    if n==2:
        return 2
    #nまでの素数を列挙するよ
    numbers = [True for x in range(n+1)]
    numbers[0] = numbers[1] = False
    #探索範囲はフェルマーの小定理より√Nまでで充分
    maximum = int(n**0.5)
    for idx, t in enumerate(numbers[:maximum+1]):
        if idx>=2 and t==True:
            for s in range(idx*2, n+1, idx):
                numbers[s]=False
    
    #trueが素数になる
    return [idx for idx, v in enumerate(numbers) if v==True]
print([x for x in eratosthenes(10000) if x>=1000]) #4桁の素数のリスト
