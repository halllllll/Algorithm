package main

import (
	"fmt"
	"sort"
)

func main() {
	var N, M int
	fmt.Scan(&N, &M)
	if N >= M {
		fmt.Println(0)
		return
	}
	A := make([]int, M)
	for i := 0; i < M; i++ {
		fmt.Scan(&A[i])
	}
	sort.Ints(A)
	difs := make([]int, M-1)
	for i := 1; i < M; i++ {
		difs[i-1] = abs(A[i-1] - A[i])
	}
	sort.Ints(difs)
	ans := 0
	for i := 0; i < M-N; i++ {
		ans += difs[i]
	}
	fmt.Println(ans)
}

func abs(x int) int {
	if x < 0 {
		x *= -1
	}
	return x
}
