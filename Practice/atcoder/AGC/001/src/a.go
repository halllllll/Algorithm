package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	L := make([]int, 2*N)
	for i := 0; i < 2*N; i++ {
		fmt.Scan(&L[i])
	}
	sort.Ints(L)
	ans := 0
	for i := 0; i < 2*N; i += 2 {
		ans += min(L[i], L[i+1])
	}
	fmt.Println(ans)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
