// gcd lcm毎回勘で書いてるよね
// py, rbで解いてたから気づかんかったけどオーバーフローするなこれ

package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	var ans int
	fmt.Scan(&ans)
	for i := 1; i < N; i++ {
		var V int
		fmt.Scan(&V)
		ans = lcm(ans, V)
	}
	fmt.Println(ans)
}

func lcm(a, b int) int {
	return a / gcd(a, b) * b
}

func gcd(a, b int) int {
	if a > b {
		a, b = b, a
	}
	for a > 0 {
		a, b = b%a, a
	}
	return b
}
