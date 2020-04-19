package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	A := make([]int, N)
	for i := 0; i < N-1; i++ {
		var j int
		fmt.Scan(&j)
		A[j-1] += 1
	}
	for _, a := range A {
		fmt.Println(a)
	}
}
