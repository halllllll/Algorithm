package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	A := make(map[int]int)
	sum := 0
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[V]++
		sum += V
	}
	var Q int
	fmt.Scan(&Q)
	for i := 0; i < Q; i++ {
		var V, C int
		fmt.Scan(&V, &C)
		x := V * A[V]
		y := C * A[V]
		sum += y - x
		A[C] += A[V]
		A[V] = 0
		fmt.Println(sum)
	}
}
