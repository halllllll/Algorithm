package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	A, S := make([]int, N), 0
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[i] = V
		S += V
	}

	if S%N != 0 {
		fmt.Println(-1)
		return
	}
	D := S / N
	ANS := 0
	L, T := 1, 0
	for _, a := range A {
		T += a
		// if T/L != D {
		if T != D*L {
			ANS += 1
		}
		L += 1

	}
	fmt.Println(ANS)
}
