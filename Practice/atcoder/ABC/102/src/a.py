# Nは2とほにゃららを2以外の因数にもつので偶数ならnで奇数なら2*n

n = int(input())
if n % 2 == 1:
    print(2 * n)
else:
    print(n)
