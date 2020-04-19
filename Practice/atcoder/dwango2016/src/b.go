package main

import "fmt"

func main() {
	var N int
	var A []int
	fmt.Scan(&N)
	A = make([]int, N-1)
	for i := 0; i < N-1; i++ {
		var j int
		fmt.Scan(&j)
		A[i] = j
	}
	ANS := make([]int, N)
	ANS[0], ANS[N-1] = A[0], A[N-2]
	for i := 1; i < N-1; i++ {
		if A[i-1] < A[i] {
			ANS[i] = A[i-1]
		} else {
			ANS[i] = A[i]
		}
	}
	for _, a := range ANS {
		fmt.Printf("%d ", a)
	}
}
