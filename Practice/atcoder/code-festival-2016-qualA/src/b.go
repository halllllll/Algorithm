package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]int, N+1)
	for i := 1; i <= N; i++ {
		fmt.Scan(&A[i])
	}
	count := 0
	for i := 1; i <= N; i++ {
		if i == A[A[i]] && A[i] == A[A[A[i]]] {
			count++
		}
	}
	fmt.Println(count / 2)
}
