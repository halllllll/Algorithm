package main

import "fmt"

func main() {
	var N, K int
	fmt.Scan(&N, &K)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		if i == 0 {
			A[i] = V
		} else {
			A[i] = A[i-1] + V
		}
	}
	ans := A[K-1]
	for i := K; i < N; i++ {
		ans += A[i] - A[i-K]
	}
	fmt.Println(ans)
}
