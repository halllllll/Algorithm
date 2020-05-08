package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[i] = V
	}
	sort.Ints(A)
	for i := 0; i < N; i++ {
		fmt.Print(A[i])
		if i < N-1 {
			fmt.Print(" ")
		} else {
			fmt.Println()
		}
	}

}
