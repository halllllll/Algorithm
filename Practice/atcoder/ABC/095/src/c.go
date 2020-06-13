// ABを買うか買わないか -> 駄目
// ABだけを買って分解する -> これが想定解らしい...
package main

import "fmt"

func main() {
	var A, B, C, X, Y int
	fmt.Scan(&A, &B, &C, &X, &Y)
	ans := int(1e18)
	for i := 0; i <= int(1e5); i++ {
		x, y := 0, 0
		if i < X {
			x = X - i
		}
		if i < Y {
			y = Y - i
		}
		ans = min(ans, 2*i*C+x*A+y*B)
	}
	fmt.Println(ans)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
