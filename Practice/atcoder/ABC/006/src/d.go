// 最長増加部分列
package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	C := make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		C[i] = V
	}
	INF := int(10e9)
	L := make([]int, N)
	for i := 0; i < N; i++ {
		L[i] = INF
	}
	length := 1
	for i := 0; i < N; i++ {
		if L[length-1] < C[i] {
			L[length] = C[i]
			length++
		} else {
			idx := sort.Search(N, func(j int) bool {
				return L[j] >= C[i]
			})
			L[idx] = C[i]
		}
	}
	fmt.Println(N - length)
}
