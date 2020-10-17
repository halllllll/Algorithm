// ncr mod pを貼って終了
// 縁から向こう側に戻るのを含めて4パターンあるので
package main

import "fmt"

func main() {
	var R, C, A1, A2, B1, B2 int
	fmt.Scan(&R, &C, &A1, &A2, &B1, &B2)
	MOD := 100000007
}

func ncr(n, r int) int {
	res := 1
	for i := 1; i <= r; i++ {
		res = res * (n - i + 1) / i
	}
	return res
}

func abs(a int) int {
	if a < 0 {
		a *= -1
	}
	return a
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
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
