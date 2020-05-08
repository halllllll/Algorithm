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
	ans := 0
	for _, a := range A {
		if ans < a {
			ans = a
		}
	}
	fmt.Println(ans)
}
