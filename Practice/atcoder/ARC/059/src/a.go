// 暴力即可
package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[i] = V
	}
	ans := int(1e9)
	for i := -100; i <= 100; i++ {
		tmp := 0
		for _, a := range A {
			tmp += (a - i) * (a - i)
		}
		ans = min(ans, tmp)
	}
	fmt.Println(ans)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
