package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	INF := int(10e9)
	L := make([]int, N)
	for i := 0; i < N; i++ {
		L[i] = INF
	}
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		idx := sort.SearchInts(L, V)
		L[idx] = V
	}
	fmt.Println(sort.SearchInts(L, INF))
}
