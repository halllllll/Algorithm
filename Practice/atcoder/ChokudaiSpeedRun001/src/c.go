package main

import (
	"fmt"
	"strings"
)

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]string, N)
	for i := 0; i < N; i++ {
		var V string
		fmt.Scan(&V)
		A[i] = V
	}
	fmt.Println(strings.Join(A, ","))
}
