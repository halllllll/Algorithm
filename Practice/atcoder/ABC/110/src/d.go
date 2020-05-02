// 難さんすう すーぱーさんすうと呼ぼう
// Mを素因数分解しといて例えばM=12としてM=(2^2) * (3^1)なるが、それぞれの因数をそれぞれの乗数ぶん振り分ける感じにした組み合わせが答え
// N = 3なら [1, 1, 1]の3つのどれかに振り分ける つまり以下
// 因数2を2つ,因数3を1つ を振り分けて、
//			[2^1, 2^1, 2^0], [3^1, 3^0, 3^0]
// 				-> [1*(2^1 * 3^1)] * [1*(2^1 * 3^0)] * [1*(2^0 * 3^0)] = 6*2*1 = 12
// あるいは
//			[2^2, 2^0, 2^0], [3^0, 3^0, 3^1] ならば
//				-> [1*(2^2 * 3^0)] * [1*(2^0 * 3^0)] * [1*(2^0 * 3^1)] = 4*1*3 = 12
// あるいは
//			[2^1, 2^1, 2^0], [3^0, 3^0, 3^1] ならば
//				-> [1*(2^1 * 3^0)] * [1*(2^1 * 3^0)] * [1*(2^0 * 3^1)] = 2*2*3 = 12
//
// 解説の""計算量はNに依らない""が意味不明だけど、説明してくれないので無視
// すーぱーさんすうの世界ではこれを重複組合せと呼ばうらしい 漢字だね 画数が多い
// n種類のものから重複を許してr個選ぶ場合の数 = nHr = (n+r-1)Cr に帰着できるらしい

// nCr mod Pなので気をつける
package main

import (
	"fmt"
	"math"
)

var MOD int

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	arr := primeFactorization(M)
	ans := 1
	MOD = int(math.Pow10(9)) + 7
	for _, v := range arr {
		ans = ans * combMod(v+N-1, v, MOD) % MOD
	}
	fmt.Println(ans)
}

func primeFactorization(x int) map[int]int {
	ret := make(map[int]int)
	for i := 2; i*i <= x; i++ {
		for x%i == 0 {
			x /= i
			ret[i] += 1
		}
	}
	if x > 1 {
		ret[x] += 1
	}
	return ret
}

func combMod(n, m, MOD int) int {
	return factorial(n, n-m+1, MOD) * pow(factorial(m, 2, MOD), MOD-2, MOD) % MOD
}

func pow(x, n, MOD int) int {
	r := 1
	for ; n > 0; n /= 2 {
		if n%2 == 1 {
			r = r * x % MOD
		}
		x = x * x % MOD
	}
	return r
}

func factorial(n, m, MOD int) int {
	r := 1
	for i := m; i <= n; i++ {
		r = r * i % MOD
	}
	return r
}
