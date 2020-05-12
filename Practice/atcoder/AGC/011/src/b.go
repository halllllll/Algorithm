package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	A := []int{}
	D := make(map[int]int)
	for i := 0; i < N; i++ {
		var j int
		fmt.Scan(&j)
		if _, ok := D[j]; ok {
			D[j] += 1
		} else {
			D[j] = 1
			A = append(A, j)
		}
	}
	sort.Ints(A)
	fmt.Println(D)
	fmt.Println(A)
	// ans := 1 // 最大値はどうせ該当する
	ans := 0
	for i := 0; i < len(A)-1; i++ {
		if 2*A[i] >= A[i+1] {
			ans += (i + 1) * D[A[i]]
		}
	}
	fmt.Println(ans)
}
