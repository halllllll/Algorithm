package main

import "fmt"

func main() {
	var N, S int
	fmt.Scan(&N, &S)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[i] = V
	}
	r := 0
	ans := 100000000000
	tmp := 0
	for l := 0; l < N; l++ {
		for r < N && tmp < S {
			tmp += A[r]
			r++
		}
		if tmp >= S {
			ans = min(ans, r-l)
		}
		if r == l {
			r++
		} else {
			tmp -= A[l]
		}
	}
	if ans < 100000000000 {
		fmt.Println(ans)
	} else {
		fmt.Println(0)
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
