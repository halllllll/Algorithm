package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)
	sum := 0
	odd := false
	for i := 0; i < N; i++ {
		var V int
		fmt.Scan(&V)
		sum += V
		if V%2 == 1 {
			odd = true
		}
	}
	if sum == N || sum%2 == 1 || (sum%2 == 0 && odd) {
		fmt.Println("first")
	} else {
		fmt.Println("second")
	}
}
