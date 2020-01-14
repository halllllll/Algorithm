# よくよくサンプル1をみたら1ずつインクリメントするので
# なんか久しぶりに前回やったコードよりまともなのを書いた気がする
n, a, b = map(int, input().split())
mins = b + a * (n - 1)
maxs = a + b * (n - 1)
print(max(0, maxs - mins + 1))
