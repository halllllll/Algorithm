// 逆をやる
package main

import "fmt"

func main() {
	var K int
	fmt.Scan(&K)
	a, b := 1, 1
	idx := 1
	for idx < K {
		a, b = b, a+b
		idx += 1
	}
	fmt.Println(a, b)
	// fmt.Println(gcd(a, b))
}

func gcd(a, b int) int {
	idx := 0
	for a > 0 {
		a, b = b%a, a
		fmt.Println(a, b)
		idx += 1
	}
	// a, b = 15, 123
	// a, b = 3, 15
	// a, b = 0, 3
	return idx
}
