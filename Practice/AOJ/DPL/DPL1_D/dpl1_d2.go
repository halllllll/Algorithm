package main

import (
	"fmt"
	"sort"
)

var N int
var A []int

func main() {
	fmt.Scan(&N)
	A = make([]int, N)
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		A[i] = V
	}
	L := make([]int, N)
	for i := 0; i < N; i++ {
		L[i] = 10000000000000000
	}
	length := 1
	L[0] = A[0]
	for i := 0; i < N; i++ {
		if A[i] > L[length-1] {
			L[length] = A[i]
			length++
		} else {
			idx := sort.Search(N, func(j int) bool { return L[j] >= A[i] })
			L[idx] = A[i]
		}
	}
	fmt.Println(length)

}
