package main

import "fmt"

func main() {
	var k int
	fmt.Scan(&k)
	ans := 0
	for p := 1; p <= k; p++ {
		for q := 1; q <= k; q++ {
			for r := 1; r <= k; r++ {
				ans += gcd(p, gcd(q, r))
			}
		}
	}
	fmt.Println(ans)
}

func gcd(a, b int) (ret int) {
	if a > b {
		a, b = b, a
	}
	for a > 0 {
		a, b = b%a, a
	}
	return b
}
